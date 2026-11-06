#!/usr/bin/env python3
"""Adapters for official schedule pages that do not publish XMLTV directly."""
import re
import urllib.request
from datetime import datetime, time, timedelta, timezone
from html.parser import HTMLParser
from zoneinfo import ZoneInfo

HUM_TV_SOURCE = "https://hum.tv/schedule/"
HUM_TV_CHANNEL_ID = "HumTV.pk"
RTV_SOURCE = "https://rtvonline.com/index.php/schedule.php"
RTV_LEGACY_SOURCES = ("https://rtvbd.tv/schedule.php", "https://www.rtvbd.tv/schedule.php")
RTV_CHANNEL_ID = "RTV.bd"
BTV_SOURCE = "https://migrate.btvlive.gov.bd/channel/BTV"
BTV_CHANNEL_ID = "BTVNational.bd"
MAASRANGA_SOURCE = "https://maasranga.tv/full-width/program-time-schedule/"
MAASRANGA_CHANNEL_ID = "MaasrangaTV.bd"
PAKISTAN_TZ = ZoneInfo("Asia/Karachi")
BANGLADESH_TZ = ZoneInfo("Asia/Dhaka")
WEEKDAYS = {
    "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
    "friday": 4, "saturday": 5, "sunday": 6,
}
TIME_RE = re.compile(r"(?<!\d)(\d{1,2}):(\d{2})\s*([AP])\.?M\.?(?![A-Z])", re.I)
GENERIC = {"schedule", "24 hour schedule", "image", "hum tv", "program", "programme"}


def _clean(value):
    return re.sub(r"\s+", " ", (value or "").replace("\xa0", " ")).strip()


class _HumScheduleParser(HTMLParser):
    """Read only named, timed shows before the page's 24-hour grid."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.events = []
        self.current_day = None
        self.pending_title = None
        self.in_h4 = False
        self.h4_text = []
        self.in_h2 = False
        self.h2_text = []
        self.done = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if self.done:
            return
        if tag == "h4":
            self.in_h4 = True
            self.h4_text = []
        elif tag == "h2" and self.current_day is not None:
            self.pending_title = None
            self.in_h2 = True
            self.h2_text = []

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "h4" and self.in_h4:
            heading = _clean("".join(self.h4_text)).lower()
            if heading in WEEKDAYS:
                self.current_day = WEEKDAYS[heading]
                self.pending_title = None
            self.in_h4 = False
            self.h4_text = []
        elif tag == "h2" and self.in_h2:
            text = _clean("".join(self.h2_text))
            match = TIME_RE.search(text)
            if match:
                self._record(_clean(text[:match.start()]), match)
            elif text:
                self.pending_title = text
            self.in_h2 = False
            self.h2_text = []

    def handle_data(self, data):
        if self.done:
            return
        if self.in_h4:
            self.h4_text.append(data)
            return
        if self.in_h2:
            self.h2_text.append(data)
            return
        text = _clean(data)
        if text.lower() == "24 hour schedule":
            self.done = True
            self.pending_title = None
            return
        if self.current_day is not None and self.pending_title:
            match = TIME_RE.search(text)
            if match:
                self._record(self.pending_title, match)

    def _record(self, title, match):
        title = _clean(title)
        if not title or title.lower() in GENERIC:
            self.pending_title = None
            return
        hour = int(match.group(1)) % 12
        if match.group(3).upper() == "P":
            hour += 12
        minute = int(match.group(2))
        if hour > 23 or minute > 59:
            self.pending_title = None
            return
        event = {
            "weekday": self.current_day,
            "hour": hour,
            "minute": minute,
            "title": title,
        }
        if not any(
            old["weekday"] == event["weekday"]
            and old["hour"] == event["hour"]
            and old["minute"] == event["minute"]
            and old["title"] == event["title"]
            for old in self.events
        ):
            self.events.append(event)
        self.pending_title = None


def fetch_hum_tv_programmes(now=None):
    """Fetch HUM TV's domestic weekly schedule and expand it to the next 7 days.

    The official page labels programme start times and separately shows an hourly
    24-hour grid. The adapter emits one-hour slots for explicit named entries only;
    image-only or unnamed slots are intentionally omitted.
    """
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now_utc = now.astimezone(timezone.utc)
    request = urllib.request.Request(
        HUM_TV_SOURCE,
        headers={
            "User-Agent": "BDIX-IPTV-Official-Schedule/1.0",
            "Accept": "text/html,application/xhtml+xml,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")

    parser = _HumScheduleParser()
    parser.feed(html)
    parser.close()
    if len(parser.events) < 14:
        raise RuntimeError(
            "Could not safely parse at least 14 explicitly timed HUM TV programme slots; "
            "the official schedule markup may have changed."
        )

    lower = now_utc - timedelta(hours=6)
    upper = now_utc + timedelta(days=7)
    local_today = now_utc.astimezone(PAKISTAN_TZ).date()
    programmes = []
    for offset in range(8):
        day = local_today + timedelta(days=offset)
        for event in parser.events:
            if event["weekday"] != day.weekday():
                continue
            start_local = datetime.combine(
                day, time(event["hour"], event["minute"]), tzinfo=PAKISTAN_TZ
            )
            stop_local = start_local + timedelta(hours=1)
            start = start_local.astimezone(timezone.utc)
            stop = stop_local.astimezone(timezone.utc)
            if stop < lower or start > upper:
                continue
            programmes.append({
                "channel_id": HUM_TV_CHANNEL_ID,
                "title": event["title"],
                "start_dt": start,
                "stop_dt": stop,
            })

    unique = {}
    for programme in programmes:
        key = (programme["start_dt"], programme["stop_dt"], programme["title"])
        unique[key] = programme
    return sorted(unique.values(), key=lambda x: (x["start_dt"], x["title"]))


RTV_WEEKDAYS = {
    "mon": 0, "monday": 0, "tue": 1, "tues": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2, "thu": 3, "thur": 3, "thurs": 3, "thursday": 3,
    "fri": 4, "friday": 4, "sat": 5, "saturday": 5, "sun": 6, "sunday": 6,
}
RTV_GENERIC = GENERIC | {"rtv", "today's schedule", "today's programme", "today's program"}
RTV_BLOCK_TAGS = {
    "address", "article", "br", "div", "footer", "h1", "h2", "h3", "h4",
    "header", "li", "main", "p", "section", "td", "th", "tr", "ul",
}
RTV_SKIP_TAGS = {"script", "style", "noscript", "svg"}


class _RtvScheduleParser(HTMLParser):
    """Extract visible lines from RTV's official weekly schedule page."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip_stack = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if self.skip_stack:
            if tag in RTV_SKIP_TAGS:
                self.skip_stack.append(tag)
            return
        if tag in RTV_SKIP_TAGS:
            self.skip_stack.append(tag)
            return
        if tag in RTV_BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if self.skip_stack:
            if tag == self.skip_stack[-1]:
                self.skip_stack.pop()
            return
        if tag in RTV_BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip_stack and data:
            self.parts.append(data)

    def text(self):
        return "".join(self.parts)


RTV_BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
RTV_BN_MONTHS = {
    "জানুয়ারি": 1, "জানুয়ারি": 1, "জানু": 1,
    "ফেব্রুয়ারি": 2, "ফেব্রুয়ারি": 2, "ফেব্রু": 2,
    "মার্চ": 3, "এপ্রিল": 4, "মে": 5, "জুন": 6, "জুলাই": 7,
    "আগস্ট": 8, "সেপ্টেম্বর": 9, "অক্টোবর": 10, "নভেম্বর": 11,
    "নভে": 11, "ডিসেম্বর": 12,
}
RTV_BN_DATE_RE = re.compile(
    r"(?P<day>\d{1,2})\s+(?P<month>"
    + "|".join(re.escape(x) for x in sorted(RTV_BN_MONTHS, key=len, reverse=True))
    + r")\s+(?P<year>\d{4})"
)
RTV_BN_TIME_RE = re.compile(
    r"(?P<period>ভোর|সকাল|দুপুর|বিকেল|সন্ধ্যা|রাত)\s*"
    r"(?P<hour>\d{1,2})\s*টা"
    r"(?:\s*(?P<minute>\d{1,2})\s*মিনিট)?"
    r"(?:\s*(?:তে|এ|য়))?"
)


def _parse_rtv_daily_programmes(text, now_utc):
    """Parse RTV's dated Bengali daily schedule without inventing stale slots."""
    normalized_text = (text or "").translate(RTV_BN_DIGITS)
    date_match = RTV_BN_DATE_RE.search(normalized_text)
    if not date_match:
        return []

    month = RTV_BN_MONTHS.get(date_match.group("month"))
    if not month:
        return []
    schedule_day = datetime(
        int(date_match.group("year")), month, int(date_match.group("day"))
    ).date()
    local_today = now_utc.astimezone(BANGLADESH_TZ).date()
    if schedule_day < local_today or schedule_day > local_today + timedelta(days=1):
        return []

    events = []
    pending = None
    for raw_line in normalized_text.splitlines():
        line = _clean(raw_line)
        if not line:
            continue
        match = RTV_BN_TIME_RE.search(line)
        if match:
            period = match.group("period")
            hour = int(match.group("hour"))
            minute = int(match.group("minute") or 0)
            if not 1 <= hour <= 12 or not 0 <= minute <= 59:
                pending = None
                continue

            day_offset = 0
            if period in {"ভোর", "সকাল"}:
                hour %= 12
            elif period == "দুপুর":
                hour = 12 if hour == 12 else hour + 12
            else:
                if period == "রাত" and hour == 12:
                    hour = 0
                    day_offset = 1
                else:
                    hour = 12 if hour == 12 else hour + 12

            title = _clean(line[match.end():])
            title = re.sub(r"^[\s\-–—:]+", "", title)
            title = re.split(r"\s*(?:->|→)\s*", title, maxsplit=1)[0].strip()
            if title and title.casefold() not in RTV_GENERIC:
                events.append({
                    "day_offset": day_offset,
                    "hour": hour,
                    "minute": minute,
                    "title": title,
                })
                pending = None
            else:
                pending = (day_offset, hour, minute)
            continue

        if pending:
            title = re.split(r"\s*(?:->|→)\s*", line, maxsplit=1)[0].strip()
            day_offset, hour, minute = pending
            pending = None
            if title and title.casefold() not in RTV_GENERIC:
                events.append({
                    "day_offset": day_offset,
                    "hour": hour,
                    "minute": minute,
                    "title": title,
                })

    unique_events = {}
    for event in events:
        key = (
            event["day_offset"], event["hour"], event["minute"],
            event["title"].casefold(),
        )
        unique_events[key] = event
    events = sorted(
        unique_events.values(),
        key=lambda x: (x["day_offset"], x["hour"], x["minute"], x["title"].casefold()),
    )
    if len(events) < 3:
        return []

    lower = now_utc - timedelta(hours=6)
    upper = now_utc + timedelta(days=7)
    programmes = []
    for current, nxt in zip(events, events[1:]):
        start_local = datetime.combine(
            schedule_day + timedelta(days=current["day_offset"]),
            time(current["hour"], current["minute"]),
            tzinfo=BANGLADESH_TZ,
        )
        stop_local = datetime.combine(
            schedule_day + timedelta(days=nxt["day_offset"]),
            time(nxt["hour"], nxt["minute"]),
            tzinfo=BANGLADESH_TZ,
        )
        duration = stop_local - start_local
        if duration <= timedelta(0) or duration > timedelta(minutes=180):
            continue
        start = start_local.astimezone(timezone.utc)
        stop = stop_local.astimezone(timezone.utc)
        if stop < lower or start > upper:
            continue
        programmes.append({
            "channel_id": RTV_CHANNEL_ID,
            "title": current["title"],
            "start_dt": start,
            "stop_dt": stop,
        })

    unique = {}
    for programme in programmes:
        key = (programme["start_dt"], programme["stop_dt"], programme["title"].casefold())
        unique[key] = programme
    return sorted(unique.values(), key=lambda x: (x["start_dt"], x["title"].casefold()))


def _parse_rtv_weekly_programmes(html, now_utc):
    """Fallback parser for the retired English weekday-based RTV schedule."""
    parser = _RtvScheduleParser()
    parser.feed(html)
    parser.close()

    weekly_events = []
    current_day = None
    pending = None
    for raw_line in parser.text().splitlines():
        line = _clean(raw_line)
        if not line:
            continue
        day_key = re.sub(r"[^a-z]", "", line.casefold())
        if day_key in RTV_WEEKDAYS:
            current_day = RTV_WEEKDAYS[day_key]
            pending = None
            continue
        match = TIME_RE.search(line)
        if match and current_day is not None:
            hour = int(match.group(1)) % 12
            if match.group(3).upper() == "P":
                hour += 12
            minute = int(match.group(2))
            if hour > 23 or minute > 59:
                pending = None
                continue
            title = _clean(line[match.end():])
            title = re.sub(r"^[\s\-–—:]+", "", title)
            title = re.split(r"\s*(?:->|→)\s*", title, maxsplit=1)[0].strip()
            if title:
                pending = None
                if title.casefold() not in RTV_GENERIC:
                    weekly_events.append({
                        "weekday": current_day, "hour": hour, "minute": minute, "title": title
                    })
            else:
                pending = (current_day, hour, minute)
            continue
        if pending:
            title = re.split(r"\s*(?:->|→)\s*", line, maxsplit=1)[0].strip()
            day, hour, minute = pending
            pending = None
            if title and title.casefold() not in RTV_GENERIC and not TIME_RE.search(title):
                weekly_events.append({
                    "weekday": day, "hour": hour, "minute": minute, "title": title
                })

    unique_events = {}
    for event in weekly_events:
        key = (event["weekday"], event["hour"], event["minute"], event["title"].casefold())
        unique_events[key] = event
    weekly_events = list(unique_events.values())
    if len(weekly_events) < 14 or len({x["weekday"] for x in weekly_events}) < 5:
        return []

    lower = now_utc - timedelta(hours=6)
    upper = now_utc + timedelta(days=7)
    local_today = now_utc.astimezone(BANGLADESH_TZ).date()
    programmes = []
    for offset in range(8):
        day = local_today + timedelta(days=offset)
        events = sorted(
            (x for x in weekly_events if x["weekday"] == day.weekday()),
            key=lambda x: (x["hour"], x["minute"], x["title"].casefold()),
        )
        for index, event in enumerate(events[:-1]):
            nxt = events[index + 1]
            start_minutes = event["hour"] * 60 + event["minute"]
            stop_minutes = nxt["hour"] * 60 + nxt["minute"]
            duration = stop_minutes - start_minutes
            if duration <= 0 or duration > 120:
                continue
            start_local = datetime.combine(
                day, time(event["hour"], event["minute"]), tzinfo=BANGLADESH_TZ
            )
            stop_local = datetime.combine(
                day, time(nxt["hour"], nxt["minute"]), tzinfo=BANGLADESH_TZ
            )
            start = start_local.astimezone(timezone.utc)
            stop = stop_local.astimezone(timezone.utc)
            if stop < lower or start > upper:
                continue
            programmes.append({
                "channel_id": RTV_CHANNEL_ID,
                "title": event["title"],
                "start_dt": start,
                "stop_dt": stop,
            })

    unique = {}
    for programme in programmes:
        key = (programme["start_dt"], programme["stop_dt"], programme["title"])
        unique[key] = programme
    return sorted(unique.values(), key=lambda x: (x["start_dt"], x["title"]))


def fetch_rtv_programmes(now=None):
    """Fetch RTV's current official daily schedule, with a legacy weekly fallback."""
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now_utc = now.astimezone(timezone.utc)
    fetch_errors = []

    # Current RTV site publishes a dated Bengali "আজ যা দেখবেন" schedule.
    request = urllib.request.Request(
        RTV_SOURCE,
        headers={
            "User-Agent": "BDIX-IPTV-Official-Schedule/1.0",
            "Accept": "text/html,application/xhtml+xml,*/*",
            "Accept-Language": "bn-BD,bn;q=0.9,en;q=0.7",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            html = response.read().decode("utf-8", errors="replace")
        parser = _RtvScheduleParser()
        parser.feed(html)
        parser.close()
        daily = _parse_rtv_daily_programmes(parser.text(), now_utc)
        if daily:
            return daily
        fetch_errors.append("rtvonline: no current dated programme slots")
    except Exception as exc:
        fetch_errors.append(f"rtvonline: {type(exc).__name__}")

    # Retain the older weekly page only as a fallback; TLS verification remains on.
    for source_url in RTV_LEGACY_SOURCES:
        request = urllib.request.Request(
            source_url,
            headers={
                "User-Agent": "BDIX-IPTV-Official-Schedule/1.0",
                "Accept": "text/html,application/xhtml+xml,*/*",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                html = response.read().decode("utf-8", errors="replace")
            weekly = _parse_rtv_weekly_programmes(html, now_utc)
            if weekly:
                return weekly
            host = source_url.split("/", 3)[2]
            fetch_errors.append(f"{host}: no valid weekly programme slots")
        except Exception as exc:
            host = source_url.split("/", 3)[2]
            fetch_errors.append(f"{host}: {type(exc).__name__}")

    raise RuntimeError(
        "Could not obtain a current official RTV schedule over verified HTTPS ("
        + "; ".join(fetch_errors)
        + ")"
    )


# BTV publishes its current/upcoming programme guide on its official live site.
# The adapter keeps only explicitly timed cards for the BTV National playlist ID.
BTV_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
BTV_MONTHS = {
    "জানু": 1, "জানুয়ারি": 1, "ফেব্রু": 2, "ফেব্রুয়ারি": 2,
    "মার্চ": 3, "এপ্রি": 4, "এপ্রিল": 4, "মে": 5, "জুন": 6,
    "জুলাই": 7, "আগস্ট": 8, "সেপ্টে": 9, "সেপ্টেম্বর": 9,
    "অক্টো": 10, "অক্টোবর": 10, "নভে": 11, "নভেম্বর": 11,
    "ডিসে": 12, "ডিসেম্বর": 12,
    "jan": 1, "january": 1, "feb": 2, "february": 2,
    "mar": 3, "march": 3, "apr": 4, "april": 4, "may": 5,
    "jun": 6, "june": 6, "jul": 7, "july": 7, "aug": 8,
    "august": 8, "sep": 9, "sept": 9, "september": 9,
    "oct": 10, "october": 10, "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}
BTV_DATE_RE = re.compile(
    r"(\d{1,2})\s+([^\s,]+),\s*(\d{4})\s*[·•]\s*"
    r"(\d{1,2}):(\d{2})\s*[–—-]\s*(\d{1,2}):(\d{2})"
)
BTV_GENERIC_TITLES = {"প্রমোশনাল/ফিলার", "সমাপ্তি", "এক্সক্লুসিভ", "schedule", "program guide"}


class _BtvScheduleParser(HTMLParser):
    """Pair BTV's programme-card headings with their explicit date/time text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.cards = []
        self.in_heading = False
        self.heading_parts = []
        self.current_title = None
        self.body_parts = []

    def _flush(self):
        if self.current_title:
            self.cards.append((self.current_title, " ".join(self.body_parts)))
        self.current_title = None
        self.body_parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "h3":
            self._flush()
            self.in_heading = True
            self.heading_parts = []

    def handle_endtag(self, tag):
        if tag.lower() == "h3" and self.in_heading:
            self.current_title = _clean("".join(self.heading_parts))
            self.in_heading = False
            self.heading_parts = []

    def handle_data(self, data):
        if self.in_heading:
            self.heading_parts.append(data)
        elif self.current_title is not None and data:
            self.body_parts.append(data)

    def close(self):
        super().close()
        self._flush()


def fetch_btv_programmes(now=None):
    """Fetch BTV's official live-site guide and convert explicit slots to XMLTV rows.

    BTV displays Bengali dates and 24-hour local times. Only programme cards with
    a parseable date and explicit start/end are emitted; no duration is inferred.
    """
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now_utc = now.astimezone(timezone.utc)
    request = urllib.request.Request(
        BTV_SOURCE,
        headers={
            "User-Agent": "BDIX-IPTV-Official-Schedule/1.0",
            "Accept": "text/html,application/xhtml+xml,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8-sig", errors="replace")

    parser = _BtvScheduleParser()
    parser.feed(html)
    parser.close()
    if not parser.cards:
        raise RuntimeError("BTV official programme guide contained no programme cards")

    lower = now_utc - timedelta(hours=6)
    upper = now_utc + timedelta(days=7)
    programmes = []
    for raw_title, body in parser.cards:
        title = _clean(raw_title)
        if not title or title.casefold() in BTV_GENERIC_TITLES:
            continue
        text = _clean(body).translate(BTV_DIGITS)
        for match in BTV_DATE_RE.finditer(text):
            day, month_name, year, sh, sm, eh, em = match.groups()
            month = BTV_MONTHS.get(month_name.casefold().rstrip("."))
            if month is None:
                continue
            try:
                start_local = datetime(
                    int(year), month, int(day), int(sh), int(sm), tzinfo=BANGLADESH_TZ
                )
                stop_local = datetime(
                    int(year), month, int(day), int(eh), int(em), tzinfo=BANGLADESH_TZ
                )
            except ValueError:
                continue
            if stop_local <= start_local:
                stop_local += timedelta(days=1)
            if stop_local - start_local > timedelta(hours=6):
                continue
            start = start_local.astimezone(timezone.utc)
            stop = stop_local.astimezone(timezone.utc)
            if stop < lower or start > upper:
                continue
            programmes.append({
                "channel_id": BTV_CHANNEL_ID,
                "title": title,
                "start_dt": start,
                "stop_dt": stop,
            })

    unique = {}
    for programme in programmes:
        key = (programme["start_dt"], programme["stop_dt"], programme["title"].casefold())
        unique[key] = programme
    if len(unique) < 8:
        raise RuntimeError(
            "BTV official guide produced fewer than 8 explicit current/future programme slots; "
            "the page markup or schedule may have changed."
        )
    return sorted(unique.values(), key=lambda x: (x["start_dt"], x["title"].casefold()))


# Maasranga TV publishes a weekly, broadcaster-maintained grid with explicit
# start/end times. The adapter preserves Bengali titles and expands only the
# published weekday/time slots; it does not invent durations.
MAASRANGA_WEEKDAYS = {
    "রবিবার": 6, "সোমবার": 0, "মঙ্গলবার": 1, "বুধবার": 2,
    "বৃহস্পতিবার": 3, "শুক্রবার": 4, "শনিবার": 5,
    "sunday": 6, "monday": 0, "tuesday": 1, "wednesday": 2,
    "thursday": 3, "friday": 4, "saturday": 5,
}
MAASRANGA_TIME_RANGE_RE = re.compile(
    r"^\s*(\d{1,2})[:.](\d{2})\s*(am|pm)?\s*[–—-]\s*"
    r"(\d{1,2})[:.](\d{2})\s*(am|pm)?\s*$",
    re.I,
)
MAASRANGA_EMPTY_TITLES = {"", "-", "—", "–", "n/a", "none"}


class _MaasrangaScheduleParser(HTMLParser):
    """Read the official weekly schedule table as rows of explicit cells."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.rows = []
        self.in_row = False
        self.in_cell = False
        self.cells = []
        self.cell_parts = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "tr":
            self.in_row = True
            self.in_cell = False
            self.cells = []
        elif tag in {"td", "th"} and self.in_row:
            self.in_cell = True
            self.cell_parts = []
        elif tag == "br" and self.in_cell:
            self.cell_parts.append(" ")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in {"td", "th"} and self.in_row and self.in_cell:
            self.cells.append(_clean(" ".join(self.cell_parts)))
            self.in_cell = False
            self.cell_parts = []
        elif tag == "tr" and self.in_row:
            if self.cells:
                self.rows.append(self.cells)
            self.in_row = False
            self.in_cell = False
            self.cells = []
            self.cell_parts = []

    def handle_data(self, data):
        if self.in_row and self.in_cell and data:
            self.cell_parts.append(data)


def _maasranga_time_range(value):
    """Return explicit local start/end minutes; infer only omitted meridiem."""
    match = MAASRANGA_TIME_RANGE_RE.match(_clean(value))
    if not match:
        return None
    sh, sm, start_ampm, eh, em, end_ampm = match.groups()
    if not start_ampm:
        return None
    sh, sm, eh, em = int(sh), int(sm), int(eh), int(em)
    if not (1 <= sh <= 12 and 1 <= eh <= 12 and 0 <= sm <= 59 and 0 <= em <= 59):
        return None

    def minutes(hour, minute, meridiem):
        hour = hour % 12
        if meridiem.casefold() == "pm":
            hour += 12
        return hour * 60 + minute

    start = minutes(sh, sm, start_ampm)
    if end_ampm:
        end = minutes(eh, em, end_ampm)
        if end <= start:
            end += 24 * 60
    else:
        same = minutes(eh, em, start_ampm)
        if same > start:
            end = same
        else:
            other_meridiem = "pm" if start_ampm.casefold() == "am" else "am"
            other = minutes(eh, em, other_meridiem)
            end = other if other > start else other + 24 * 60

    duration = end - start
    if duration <= 0 or duration > 6 * 60:
        return None
    return start, end


def fetch_maasranga_programmes(now=None):
    """Fetch Maasranga's official weekly grid and expand explicit slots for 8 days."""
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now_utc = now.astimezone(timezone.utc)
    request = urllib.request.Request(
        MAASRANGA_SOURCE,
        headers={
            "User-Agent": "BDIX-IPTV-Official-Schedule/1.0",
            "Accept": "text/html,application/xhtml+xml,*/*",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8-sig", errors="replace")

    parser = _MaasrangaScheduleParser()
    parser.feed(html)
    parser.close()

    header_index = None
    day_columns = {}
    for index, row in enumerate(parser.rows):
        normalized = [_clean(cell).casefold() for cell in row]
        found = {
            MAASRANGA_WEEKDAYS[cell]: col
            for col, cell in enumerate(normalized)
            if cell in MAASRANGA_WEEKDAYS
        }
        if len(found) == 7 and len(row) >= 8:
            header_index = index
            day_columns = found
            break
    if header_index is None:
        raise RuntimeError("Maasranga official schedule has no complete seven-day table")

    weekly_events = []
    for row in parser.rows[header_index + 1:]:
        if len(row) < 8:
            continue
        time_range = _maasranga_time_range(row[0])
        if not time_range:
            continue
        start_minutes, end_minutes = time_range
        for weekday, column in day_columns.items():
            if column >= len(row):
                continue
            title = _clean(row[column])
            if title.casefold() in MAASRANGA_EMPTY_TITLES:
                continue
            weekly_events.append({
                "weekday": weekday,
                "start_minutes": start_minutes,
                "end_minutes": end_minutes,
                "title": title,
            })

    unique_weekly = {
        (event["weekday"], event["start_minutes"], event["end_minutes"], event["title"].casefold()): event
        for event in weekly_events
    }
    weekly_events = list(unique_weekly.values())
    if len(weekly_events) < 20 or len({event["weekday"] for event in weekly_events}) < 5:
        raise RuntimeError(
            "Maasranga weekly schedule returned too few explicit weekday slots; "
            "the official table may have changed."
        )

    local_today = now_utc.astimezone(BANGLADESH_TZ).date()
    lower = now_utc - timedelta(hours=6)
    upper = now_utc + timedelta(days=7)
    programmes = []
    for offset in range(8):
        day = local_today + timedelta(days=offset)
        for event in weekly_events:
            if event["weekday"] != day.weekday():
                continue
            start_day_offset, start_minute_of_day = divmod(event["start_minutes"], 24 * 60)
            end_day_offset, end_minute_of_day = divmod(event["end_minutes"], 24 * 60)
            start_day = day + timedelta(days=start_day_offset)
            stop_day = day + timedelta(days=end_day_offset)
            start_local = datetime.combine(
                start_day, time(start_minute_of_day // 60, start_minute_of_day % 60),
                tzinfo=BANGLADESH_TZ,
            )
            stop_local = datetime.combine(
                stop_day, time(end_minute_of_day // 60, end_minute_of_day % 60),
                tzinfo=BANGLADESH_TZ,
            )
            start = start_local.astimezone(timezone.utc)
            stop = stop_local.astimezone(timezone.utc)
            if stop <= start or stop < lower or start > upper:
                continue
            programmes.append({
                "channel_id": MAASRANGA_CHANNEL_ID,
                "title": event["title"],
                "start_dt": start,
                "stop_dt": stop,
            })

    unique = {}
    for programme in programmes:
        key = (programme["start_dt"], programme["stop_dt"], programme["title"].casefold())
        unique[key] = programme
    if not unique:
        raise RuntimeError("Maasranga official schedule produced no current/future programme slots")
    return sorted(unique.values(), key=lambda item: (item["start_dt"], item["title"].casefold()))

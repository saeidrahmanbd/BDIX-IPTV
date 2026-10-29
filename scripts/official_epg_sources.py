#!/usr/bin/env python3
"""Adapters for official schedule pages that do not publish XMLTV directly."""
import re
import urllib.request
from datetime import datetime, time, timedelta, timezone
from html.parser import HTMLParser
from zoneinfo import ZoneInfo

HUM_TV_SOURCE = "https://hum.tv/schedule/"
HUM_TV_CHANNEL_ID = "HumTV.pk"
RTV_SOURCE = "https://www.rtvbd.tv/schedule.php"
RTV_CHANNEL_ID = "RTV.bd"
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


def fetch_rtv_programmes(now=None):
    """Fetch RTV's official weekly schedule, deriving only short adjacent slots.

    The page provides weekday, named programme, and start-time entries but no
    explicit stop times. Emit a slot only when the next start that day is at
    most 120 minutes later. Omit wider gaps and each day's final listing rather
    than inventing end times. Applies only to exact RTV.bd.
    """
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now_utc = now.astimezone(timezone.utc)
    # The www host has intermittently failed certificate-chain validation.
    # Try the apex HTTPS host first, then the established www endpoint; TLS
    # verification stays enabled for both attempts.
    html = None
    fetch_errors = []
    for source_url in ("https://rtvbd.tv/schedule.php", RTV_SOURCE):
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
            break
        except Exception as exc:
            host = source_url.split("/", 3)[2]
            fetch_errors.append(f"{host}: {type(exc).__name__}")
    if html is None:
        raise RuntimeError(
            "Could not fetch the official RTV schedule over verified HTTPS ("
            + "; ".join(fetch_errors)
            + ")"
        )

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
        raise RuntimeError(
            "RTV schedule parsing returned too few explicit named weekday entries; "
            "the official page markup may have changed."
        )

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

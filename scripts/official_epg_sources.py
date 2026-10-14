#!/usr/bin/env python3
"""Adapters for official schedule pages that do not publish XMLTV directly."""
import re
import urllib.request
from datetime import datetime, time, timedelta, timezone
from html.parser import HTMLParser
from zoneinfo import ZoneInfo

HUM_TV_SOURCE = "https://hum.tv/schedule/"
HUM_TV_CHANNEL_ID = "HumTV.pk"
PAKISTAN_TZ = ZoneInfo("Asia/Karachi")
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

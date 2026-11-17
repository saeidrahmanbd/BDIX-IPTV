"""Country-independent genre precedence for the International playlist."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import reorganize_international_playlist as organizer


def classify(name, country, group="International"):
    attrs = {
        "tvg-country": country,
        "tvg-id": f"custom.{name.lower().replace(' ', '')}.{country.lower()}",
        "tvg-name": name,
    }
    return organizer.classify(attrs, name, group, country)


def test_foreign_sports_stays_in_sports():
    assert classify("ESPN", "US")[0] == "Sports"


def test_foreign_kids_stays_in_kids():
    assert classify("Cartoon Network", "US")[0] == "Kids"


def test_foreign_documentary_stays_in_documentary_group():
    assert classify("National Geographic", "US")[0] == "Documentary & Wildlife"


def test_foreign_religious_stays_in_religious_group():
    assert classify("Quran TV", "SA")[0] == "Religious"


def test_foreign_news_stays_in_news_group():
    assert classify("BBC News", "GB")[0] == "News"


def test_indian_sports_is_not_demoted_to_indian_country_group():
    assert classify("Star Sports", "IN", "Indian Entertainment")[0] == "Sports"


def test_music_and_movie_remain_in_country_groups():
    assert classify("Classic Movies", "US")[0] == "__FOREIGN__"
    assert classify("Music Channel", "US")[0] == "__FOREIGN__"

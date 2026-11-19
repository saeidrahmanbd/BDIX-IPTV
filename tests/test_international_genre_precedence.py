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


def test_foreign_sports_is_quarantined_to_review():
    assert classify("ESPN", "US")[0] == "Review"


def test_foreign_kids_is_quarantined_to_review():
    assert classify("Cartoon Network", "US")[0] == "Review"


def test_foreign_documentary_is_quarantined_to_review():
    assert classify("National Geographic", "US")[0] == "Review"


def test_foreign_religious_is_quarantined_to_review():
    assert classify("Quran TV", "SA")[0] == "Review"


def test_foreign_news_is_quarantined_to_review():
    assert classify("BBC News", "GB")[0] == "Review"


def test_indian_sports_is_not_demoted_to_indian_country_group():
    assert classify("Star Sports", "IN", "Indian Entertainment")[0] == "Sports"


def test_music_and_movie_remain_in_country_groups():
    assert classify("Classic Movies", "US")[0] == "__FOREIGN__"
    assert classify("Music Channel", "US")[0] == "__FOREIGN__"


def test_existing_indian_news_and_religious_legacy_groups_are_preserved():
    assert classify("India Today", "IN", "Indian Entertainment")[0] == "News"
    assert classify("Islamic TV", "IN", "Religious")[0] == "Religious"


def test_bangladesh_and_pakistan_keep_genre_freedom():
    assert classify("Somoy TV", "BD", "News")[0] == "News"
    assert classify("PTV Sports", "PK", "Sports")[0] == "Sports"

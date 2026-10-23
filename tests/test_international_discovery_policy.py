#!/usr/bin/env python3
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import discover_international_channels as discovery
class InternationalDiscoveryPolicyTests(unittest.TestCase):
    def classify(self,name,group,country=None,tvg_id=None,language=None):
        a={'group-title':group}
        if country:a['tvg-country']=country
        if tvg_id:a['tvg-id']=tvg_id
        if language:a['tvg-language']=language
        return discovery.policy(a,name)
    def test_movies_are_allowed_for_any_country(self):
        self.assertEqual(self.classify('Cinema World','Movies','NP','CinemaWorld.np'),('International',None,'NP'))
    def test_music_is_allowed_for_any_country(self):
        self.assertEqual(self.classify('World Music','Music','TH','WorldMusic.th'),('International',None,'TH'))
    def test_country_group_name_is_available(self):
        self.assertEqual(discovery.country_group('NP'),'Nepal'); self.assertEqual(discovery.country_group('TH'),'Thailand'); self.assertEqual(discovery.country_group('JP'),'Japan')
    def test_country_threshold_is_five(self): self.assertEqual(discovery.COUNTRY_THRESHOLD,5)
    def test_bangladesh_news_is_allowed(self): self.assertEqual(self.classify('Channel 24','News','BD','Channel24.bd'),('Bangladesh',None,'BD'))
    def test_foreign_news_is_rejected(self):
        group,reason,country=self.classify('World News','News','US','WorldNews.us'); self.assertIsNone(group); self.assertEqual(reason,'non-Bangladeshi or unverified-country news channel')
    def test_unknown_country_news_is_rejected(self):
        group,reason,country=self.classify('Global News','General',None,'GlobalNews.custom'); self.assertIsNone(group); self.assertEqual(reason,'non-Bangladeshi or unverified-country news channel')
    def test_foreign_news_brand_is_rejected(self):
        group,reason,country=self.classify('CNBC World','Business','SG','CNBCWorld.sg'); self.assertIsNone(group); self.assertEqual(reason,'non-Bangladeshi or unverified-country news channel')
    def test_islamic_religious_channel_is_allowed(self): self.assertEqual(self.classify('Sunnah TV','Religious','SA','SunnahTV.sa'),('Religious',None,'SA'))
    def test_known_islamic_network_is_allowed(self): self.assertEqual(self.classify('MTA International','Religious','GB','MTAInternational.uk'),('Religious',None,'GB'))
    def test_non_islamic_religious_channel_is_rejected(self):
        group,reason,country=self.classify('Gospel TV','Religious','US','GospelTV.us'); self.assertIsNone(group); self.assertEqual(reason,'non-Islamic religious channel')
    def test_hindu_religious_channel_is_rejected(self):
        group,reason,country=self.classify('Dharma TV','General','IN','DharmaTV.in'); self.assertIsNone(group); self.assertEqual(reason,'non-Islamic religious channel')
    def test_religious_content_is_rejected_even_if_music(self):
        group,reason,country=self.classify('Hindu Bhakti Music','Music','IN','BhaktiMusic.in'); self.assertIsNone(group); self.assertEqual(reason,'non-Islamic religious channel')
    def test_country_is_inferred_from_id_suffix(self):
        group,reason,country=self.classify('World News','News',None,'WorldNews.uk@HD'); self.assertIsNone(group); self.assertEqual(country,'GB')
    def test_sports_and_documentaries_are_allowed(self):
        self.assertEqual(self.classify('World Sport','Sports','US','WorldSport.us')[:2],('Sports',None)); self.assertEqual(self.classify('Nature World','Documentary','ZA','NatureWorld.za')[:2],('Documentary & Wildlife',None))
    def test_tokenized_urls_are_rejected_without_playback(self): self.assertEqual(discovery.safe_url('https://example.org/live.m3u8?token=abc'),False)
    def test_plain_stream_urls_are_accepted_by_syntax_only(self): self.assertEqual(discovery.safe_url('https://example.org/channel/index.m3u8'),True)
if __name__=='__main__':unittest.main()

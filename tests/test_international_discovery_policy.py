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
    def test_country_with_four_playlist_identities_does_not_get_a_group(self):
        self.assertNotIn("AT", discovery.qualified_country_groups({"AT": {"a","b","c","d"}}))
    def test_country_with_five_playlist_identities_gets_a_group(self):
        self.assertIn("AT", discovery.qualified_country_groups({"AT": {"a","b","c","d","e"}}))
    def test_country_can_qualify_from_existing_staged_and_new_primary_channels(self):
        existing={"AT": {"a","b","c"}}
        added={"AT": {"d","e"}}
        self.assertIn("AT", discovery.qualified_country_groups(existing,added))
    def test_under_threshold_general_channel_goes_to_new_channels(self):
        self.assertEqual(discovery.primary_target("International","AT",set()),"New Channels")
    def test_qualified_country_gets_its_own_group(self):
        self.assertEqual(discovery.primary_target("International","AT",{"AT"}),"Austria")
    def test_content_groups_do_not_accidentally_create_country_groups(self):
        self.assertFalse(discovery.counts_toward_country_group("Kids","AT"))
        self.assertTrue(discovery.counts_toward_country_group("New Channels","AT"))
        self.assertTrue(discovery.counts_toward_country_group("International","AT"))
    def test_category_registry_only_lists_groups_present_in_playlist(self):
        groups=discovery.category_registry(["Bangladesh","United Kingdom","International","Backup"])
        self.assertEqual(groups,discovery.FIXED_GROUPS+["United Kingdom"]+discovery.TAIL_GROUPS)

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
    def test_3abn_kids_is_rejected_even_in_kids_category(self):
        group,reason,country=self.classify('3ABN Kids','Kids','US','3ABNKids.us@SD'); self.assertIsNone(group); self.assertEqual(reason,'non-Islamic religious channel')
    def test_3abn_network_alias_is_rejected(self):
        group,reason,country=self.classify('3ABN Latino','General','US','3ABNLatino.us'); self.assertIsNone(group); self.assertEqual(reason,'non-Islamic religious channel')
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

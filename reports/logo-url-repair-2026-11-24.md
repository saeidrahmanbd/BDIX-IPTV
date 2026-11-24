# Local Logo URL Repair Report — 2026-11-24

## Scope
Audited the current `main` branch of `saeidrahmanbd/BDIX-IPTV` using the Git tree and exact playlist blobs.

## Repairs staged
| Playlist | Relative logo paths converted to full repository raw URLs | Missing logo attributes filled from a unique exact `tvg-id` match |
|---|---:|---:|
| IPTV-Playlist.m3u | 411 | 0 |
| International-Playlist.m3u | 8 | 16 |

- Every retained and newly assigned logo URL uses the repository-owned `https://raw.githubusercontent.com/saeidrahmanbd/BDIX-IPTV/main/logos/...` namespace.
- Every referenced logo path was checked for a matching file path in the repository Git tree; **0 missing asset paths** were found.
- Existing canonical full raw URLs were preserved.
- Channel rows, stream URLs, channel order, groups, channel numbers, and unrelated metadata were not intentionally changed.

## Remaining logo gaps
International-Playlist.m3u still has **407 entries without a `tvg-logo` attribute** after safe repairs. No arbitrary, generic, or visually similar logo was assigned. These need exact channel identification and authentic local artwork.

| Playlist line | tvg-id | Channel |
|---:|---|---|
| 177 | `custom.asian-sony-max-2` | Asian Sony Max 2 |
| 395 | `RajMusicTelugu.in@SD` | Raj Music Telugu |
| 683 | `custom.rengoni-tv` | Rengoni TV |
| 887 | `cinebox.bg@SD` | cine.box |
| 1041 | `custom.cedros-tv-cr-music` | Cedros TV |
| 1125 | `DanceTVAlgorhythm.ee@SD` | DanceTV Algorhythm |
| 1165 | `PersianaVibe.fr@HD` | Persiana Vibe |
| 1859 | `TV21International.ru@SD` | TV 21 International |
| 1891 | `Tarab.sa@SD` | Tarab |
| 2421 | `MyTimeMovieNetwork.us@SD` | MyTime Movie Network (US) |
| 2679 | `AlloCine.cm@SD` | Allo Cine |
| 2689 | `custom.asia-flix-tv-ph-movie` | Asia Flix TV |
| 2695 | `custom.bigscreen-tv-ph-movie` | Bigscreen TV |
| 2845 | `custom.sine-plus-ph-movie` | Sine Plus |
| 2893 | `custom.bdix.news21-bangla` | NEWS 21 BANGLA |
| 3131 | `custom.bdix.travelxp-bangla` | Travel XP Bangla |
| 3231 | `Chikitoonz.pe@SD` | Chikitoonz |
| 3279 | `EKids.bg@SD` | EKids |
| 3471 | `custom.al-sunnah-tv` | Al Sunnah TV |
| 3507 | `custom.peace-tv-tw8cm` | Peace TV |
| 3519 | `custom.saudi-quran-y9quu` | Saudi Quran |
| 3595 | `CRTV.cl@SD` | CRTV (Chile) |
| 3661 | `FloRacing.us@HD` | FloRacing |
| 3891 | `custom.24-7-xxx-abella-danger` | Abella Danger |
| 3893 | `custom.24-7-xxx-aj-applegate` | AJ Applegate |
| 3895 | `custom.alba-2` | Alba 2 |
| 3897 | `custom.alba-3` | Alba 3 |
| 3899 | `custom.alba-4` | Alba 4 |
| 3901 | `custom.24-7-xxx-alexis-texas` | Alexis Texas |
| 3903 | `custom.24-7-xxx-alura-jenson` | Alura Jenson |
| 3905 | `custom.24-7-xxx-amateur` | Amateur |
| 3907 | `custom.xxx-anal` | Anal |
| 3909 | `custom.xxx-anal-mom` | Anal Mom |
| 3911 | `custom.xxx-anal-teen-angels` | Anal Teen Angels |
| 3913 | `custom.24-7-xxx-angel-smalls` | Angel Smalls |
| 3915 | `custom.24-7-xxx-angela-white` | Angela White |
| 3917 | `AsiaN.kr` | AsiaN |
| 3919 | `custom.24-7-xxx-ass-parade` | Ass Parade |
| 3921 | `custom.24-7-xxx-ava-devine` | Ava Devine |
| 3923 | `BabesTV.us` | Babes TV |
| 3925 | `custom.babes-tv-russia` | Babes TV Russia |
| 3927 | `custom.xxx-bang-bus` | Bang Bus |
| 3929 | `BangU.us` | Bang U |
| 3931 | `custom.24-7-xxx-bangbus` | Bangbus |
| 3933 | `custom.24-7-xxx-bbc-big-ass` | BBC Big Ass |
| 3935 | `custom.24-7-xxx-bbw` | BBW |
| 3937 | `custom.24-7-xxx-bdsm` | BDSM |
| 3939 | `custom.24-7-xxx-big-ass` | Big Ass |
| 3941 | `custom.xxx-big-ass` | Big Ass |
| 3943 | `custom.xxx-big-dick` | Big Dick |
| 3945 | `custom.24-7-xxx-big-tits` | Big Tits |
| 3947 | `custom.xxx-big-tits` | Big Tits |
| 3953 | `custom.xxx-blowjob` | Blowjob |
| 3955 | `custom.xxx-brand-new-amateurs` | Brand New Amateurs |
| 3957 | `custom.xxx-brazzers-europe` | Brazzers Europe |
| 3959 | `custom.xxx-brazzers-extra` | Brazzers Extra |
| 3961 | `custom.24-7-xxx-brazzers-rated` | Brazzers Rated |
| 3963 | `custom.24-7-xxx-brazzers-rated-2` | Brazzers Rated 2 |
| 3965 | `custom.24-7-xxx-brazzzers-1` | Brazzzers 1 |
| 3967 | `custom.24-7-xxx-brazzzers-2` | Brazzzers 2 |
| 3969 | `custom.24-7-xxx-brazzzers-3` | Brazzzers 3 |
| 3971 | `custom.24-7-xxx-bridgette-b` | Bridgette B |
| 3973 | `custom.brunette` | Brunette |
| 3975 | `custom.xxx-brunette` | Brunette |
| 3977 | `custom.24-7-xxx-casting-couch` | Casting Couch |
| 3979 | `custom.24-7-xxx-cathy-heaven` | Cathy Heaven |
| 3981 | `custom.24-7-xxx-cherie-deville` | Cherie Deville |
| 3983 | `custom.xxx-compilation` | Compilation |
| 3989 | `custom.xxx-cum-perfection` | Cum Perfection |
| 3991 | `custom.xxx-day-with-a-pornstar` | Day With A Pornstar |
| 3993 | `custom.24-7-xxx-dee-williams` | Dee Williams |
| 3995 | `custom.xxx-dorcel-club` | Dorcel Club |
| 3997 | `custom.24-7-xxx-ebony` | Ebony |
| 3999 | `custom.24-7-xxx-elsa-jean` | Elsa Jean |
| 4001 | `custom.xxx-ero-xxx` | Ero Xxx |
| 4003 | `custom.xxx-erox-xxx-hd` | Erox XXX |
| 4005 | `custom.xxx-euro-girls-on-girls` | Euro Girls On Girls |
| 4007 | `custom.24-7-xxx-evil-angel` | Evil Angel |
| 4009 | `custom.xxx-evil-angel-hd` | Evil Angel |
| 4011 | `custom.xxx-evolved-fights` | Evolved Fights |
| 4013 | `custom.exxxotica-tv` | Exxxotica TV |
| 4015 | `custom.24-7-xxx-fake-taxi-1` | Fake Taxi 1 |
| 4017 | `custom.24-7-xxx-fake-taxi-3` | Fake Taxi 3 |
| 4019 | `custom.fap-tv-6` | Fap TV 6 |
| 4021 | `custom.xxx-fetish` | Fetish |
| 4023 | `custom.xxx-gangbang` | Gangbang |
| 4025 | `custom.24-7-xxx-gay-2` | Gay 2 |
| 4027 | `custom.24-7-xxx-gay-3` | Gay 3 |
| 4029 | `custom.24-7-xxx-gay-latin` | Gay Latin |
| 4031 | `custom.xxx-glory-hole` | Glory Hole |
| 4033 | `custom.24-7-xxx-gloryhole` | Gloryhole |
| 4035 | `custom.24-7-xxx-group` | Group |
| 4037 | `custom.24-7-xxx-group-2` | Group 2 |
| 4039 | `custom.24-7-xxx-hardcore` | Hardcore |
| 4041 | `custom.xxx-hardcore` | Hardcore |
| 4043 | `custom.24-7-xxx-hilary-scott` | Hilary Scott |
| 4045 | `custom.24-7-xxx-holly-hendrix` | Holly Hendrix |
| 4047 | `custom.xxx-hookup-hotshot` | Hookup Hotshot |
| 4049 | `custom.xxx-hot-guys-fuck` | Hot Guys Fuck |
| 4051 | `custom.xxx-hustler` | Hustler |
| 4053 | `custom.xxx-interracial` | Interracial |
| 4055 | `custom.24-7-xxx-jada-stevens` | Jada Stevens |
| 4057 | `custom.24-7-xxx-jasmine-jae` | Jasmine Jae |
| 4059 | `custom.24-7-xxx-karma-rx` | Karma RX |
| 4061 | `custom.24-7-xxx-kelly-divine` | Kelly Divine |
| 4063 | `custom.24-7-xxx-kelsie-monroe` | Kelsie Monroe |
| 4065 | `custom.24-7-xxx-kenzie-reeves` | Kenzie Reeves |
| 4071 | `LEOTV.cz` | LEO TV |
| 4073 | `custom.xxx-lesbian` | Lesbian |
| 4075 | `custom.24-7-xxx-lisa-ann` | Lisa Ann |
| 4077 | `custom.live-cams` | Live Cams |
| 4079 | `custom.xxx-live-cams` | Live Cams |
| 4081 | `custom.24-7-xxx-london-keyes` | London Keyes |
| 4083 | `custom.24-7-xxx-luna-star` | Luna Star |
| 4085 | `custom.adultm3u-com-anal` | m3u.Com Anal |
| 4087 | `custom.adultm3u-com-asian` | m3u.Com Asian |
| 4089 | `custom.adultm3u-com-big-ass` | m3u.Com Big Ass |
| 4091 | `custom.adultm3u-com-big-dick` | m3u.Com Big Dick |
| 4093 | `custom.adultm3u-com-big-tits` | m3u.Com Big Tits |
| 4095 | `custom.adultm3u-com-blonde` | m3u.Com Blonde |
| 4097 | `custom.adultm3u-com-blowjob` | m3u.Com Blowjob |
| 4099 | `custom.adultm3u-com-brunette` | m3u.Com Brunette |
| 4101 | `custom.adultm3u-com-compilation` | m3u.Com Compilation |
| 4103 | `custom.adultm3u-com-cuckold` | m3u.Com Cuckold |
| 4105 | `custom.adultm3u-com-fetish` | m3u.Com Fetish |
| 4107 | `custom.adultm3u-com-gangbang` | m3u.Com Gangbang |
| 4109 | `custom.adultm3u-com-hardcore` | m3u.Com Hardcore |
| 4111 | `custom.adultm3u-com-interracial` | m3u.Com Interracial |
| 4113 | `custom.adultm3u-com-latina` | m3u.Com Latina |
| 4115 | `custom.adultm3u-com-lesbian` | m3u.Com Lesbian |
| 4117 | `custom.adultm3u-com-live-cams` | m3u.Com Live Cams |
| 4119 | `custom.adultm3u-com-pornstar` | m3u.Com Pornstar |
| 4121 | `custom.adultm3u-com-pov` | m3u.Com Pov |
| 4123 | `custom.adultm3u-com-rough` | m3u.Com Rough |
| 4125 | `custom.adultm3u-com-russian` | m3u.Com Russian |
| 4127 | `custom.adultm3u-com-threesome` | m3u.Com Threesome |
| 4129 | `custom.24-7-xxx-mature` | Mature |
| 4131 | `custom.xxx-mctv-big-dick` | Mctv Big Dick |
| 4133 | `custom.xxx-mctv-big-tits` | Mctv Big Tits |
| 4135 | `custom.xxx-mctv-pornstar` | Mctv Pornstar |
| 4137 | `custom.xxx-mctv-rough` | Mctv Rough |
| 4139 | `custom.24-7-xxx-metro` | Metro |
| 4141 | `custom.24-7-xxx-mia-khalifa` | Mia Khalifa |
| 4143 | `custom.xxx-mia-khalifa` | Mia Khalifa |
| 4145 | `custom.adultm3u-com-milf` | Milf |
| 4147 | `custom.xxx-milf` | Milf |
| 4149 | `custom.24-7-xxx-milfs` | Milfs |
| 4151 | `custom.24-7-xxx-milfs-stepmom` | Milfs Stepmom |
| 4153 | `custom.24-7-xxx-mom-lovers` | Mom Lovers |
| 4155 | `MusicBoxSexy.cz@SD` | Music Box Sexy |
| 4157 | `custom.xxx-my-daughter-s-hot-friend` | My Daughter's Hot Friend |
| 4159 | `custom.24-7-xxx-my-dirty-maid` | My Dirty Maid |
| 4161 | `custom.24-7-xxx-my-first-sex-teacher` | My FIrst Sex Teacher |
| 4163 | `custom.24-7-xxx-my-friends-hot-mom` | My Friends Hot Mom |
| 4165 | `MyCamTVAnal.cy` | MyCam TV Anal |
| 4167 | `MyCamTVBlowjob.cy` | MyCam TV Blowjob |
| 4169 | `MyCamTVMILF.cy` | MyCam TV MILF |
| 4171 | `custom.mycamtv-arab-girls` | Mycamtv Arab Girls |
| 4173 | `custom.mycamtv-asian-girls` | Mycamtv Asian Girls |
| 4175 | `custom.mycamtv-big-ass-girls` | Mycamtv Big Ass Girls |
| 4177 | `custom.mycamtv-blonde-girls` | Mycamtv Blonde Girls |
| 4179 | `custom.mycamtv-brunette-girls` | Mycamtv Brunette Girls |
| 4181 | `custom.mycamtv-ebony-girls` | Mycamtv Ebony Girls |
| 4183 | `custom.mycamtv-girls-squirt` | Mycamtv Girls Squirt |
| 4185 | `custom.mycamtv-latina-girls` | Mycamtv Latina Girls |
| 4187 | `custom.mycamtv-mature` | Mycamtv Mature |
| 4189 | `custom.mycamtv-medium-girls` | Mycamtv Medium Girls |
| 4191 | `custom.mycamtv-skinny-girls` | Mycamtv Skinny Girls |
| 4193 | `custom.mycamtv-white-girls` | Mycamtv White Girls |
| 4195 | `custom.xxx-naughty-america` | Naughty America |
| 4197 | `custom.24-7-xxx-nicole-doshi` | Nicole Doshi |
| 4199 | `custom.24-7-xxx-nicolette-shea` | Nicolette Shea |
| 4201 | `custom.24-7-xxx-nina-elle` | Nina Elle |
| 4203 | `custom.xxx-o-la-la` | O LA LA |
| 4205 | `custom.24-7-xxx-only-fans-jade-bunny` | Only Fans Jade Bunny |
| 4207 | `PenthouseAfterMidnight.us` | Penthouse After Midnight |
| 4209 | `PenthouseBlack.us` | Penthouse Black |
| 4211 | `PenthouseNaughtyNights.us` | Penthouse Naughty Nights |
| 4213 | `PenthousePassion.us` | Penthouse Passion |
| 4215 | `PenthouseRealityTV.us` | Penthouse Reality TV |
| 4217 | `custom.penthouse-tv` | Penthouse TV |
| 4219 | `custom.pink-erotic-1` | Pink Erotic 1 |
| 4221 | `custom.xxx-pink-erotic-2` | Pink Erotic 2 |
| 4223 | `custom.xxx-pink-erotic-3` | Pink Erotic 3 |
| 4225 | `custom.xxx-pink-erotic-4` | Pink Erotic 4 |
| 4227 | `custom.xxx-pink-erotic-5` | Pink Erotic 5 |
| 4229 | `custom.xxx-pink-erotic-6` | Pink Erotic 6 |
| 4231 | `custom.xxx-pink-erotic-7` | Pink Erotic 7 |
| 4233 | `custom.xxx-pink-erotic-8` | Pink Erotic 8 |
| 4235 | `custom.pornbox-4k-baeb` | PORNBOX 4K: BAEB |
| 4237 | `custom.pornbox-4k-bbc-pie` | PORNBOX 4K: BBC PIE |
| 4239 | `custom.pornbox-4k-cum-4k` | PORNBOX 4K: CUM |
| 4241 | `custom.pornbox-4k-girl-cum` | PORNBOX 4K: GIRL CUM |
| 4243 | `custom.pornbox-4k-jays-pov` | PORNBOX 4K: JAYS POV |
| 4245 | `custom.pornbox-4k-lubed-porn` | PORNBOX 4K: LUBED PORN |
| 4247 | `custom.pornbox-4k-nanny-spy` | PORNBOX 4K: NANNY SPY |
| 4249 | `custom.pornbox-4k-spank-monster` | PORNBOX 4K: SPANK MONSTER |
| 4251 | `custom.pornbox-4k-spy-fam` | PORNBOX 4K: SPY FAM |
| 4253 | `custom.pornbox-4k-tiny-4k` | PORNBOX 4K: TINY |
| 4255 | `custom.pornbox-gay-beefcake-hunter` | PORNBOX GAY: BEEFCAKE HUNTER |
| 4257 | `custom.pornbox-gay-boy-fun` | PORNBOX GAY: BOY FUN |
| 4259 | `custom.pornbox-gay-man` | PORNBOX GAY: MAN |
| 4261 | `custom.pornbox-1111-customs` | PORNBOX: 1111 CUSTOMS |
| 4263 | `custom.pornbox-adult-time` | PORNBOX: ADULT TIME |
| 4265 | `custom.pornbox-alex-legend` | PORNBOX: ALEX LEGEND |
| 4267 | `custom.pornbox-all-group-sex` | PORNBOX: ALL GROUP SEX |
| 4269 | `custom.pornbox-amateur-euro` | PORNBOX: AMATEUR EURO |
| 4271 | `custom.pornbox-asian-footjob` | PORNBOX: ASIAN FOOTJOB |
| 4273 | `custom.pornbox-atk-girlfriends` | PORNBOX: ATK GIRLFRIENDS |
| 4275 | `custom.pornbox-av-taxi` | PORNBOX: AV TAXI |
| 4277 | `custom.pornbox-babes` | PORNBOX: BABES |
| 4279 | `custom.pornbox-bang-bros-network` | PORNBOX: BANG BROS NETWORK |
| 4281 | `custom.pornbox-big-booty-city` | PORNBOX: BIG BOOTY CITY |
| 4283 | `custom.pornbox-blacked` | PORNBOX: BLACKED |
| 4285 | `custom.pornbox-blow-me-pov` | PORNBOX: BLOW ME POV |
| 4287 | `custom.pornbox-box-of-porn` | PORNBOX: BOX OF PORN |
| 4289 | `custom.pornbox-bratty-sis` | PORNBOX: BRATTY SIS |
| 4291 | `custom.pornbox-brazzers` | PORNBOX: BRAZZERS |
| 4293 | `custom.pornbox-bums-bus` | PORNBOX: BUMS BUS |
| 4295 | `custom.pornbox-casting-couch` | PORNBOX: CASTING COUCH |
| 4297 | `custom.pornbox-dagfs` | PORNBOX: DAGFS |
| 4299 | `custom.pornbox-ddf-busty` | PORNBOX: DDF BUSTY |
| 4301 | `custom.pornbox-deeper` | PORNBOX: DEEPER |
| 4303 | `custom.pornbox-digital-playground` | PORNBOX: DIGITAL PLAYGROUND |
| 4305 | `custom.pornbox-dog-house` | PORNBOX: DOG HOUSE |
| 4307 | `custom.pornbox-dogfart-network` | PORNBOX: DOGFART NETWORK |
| 4309 | `custom.pornbox-dorcel-club` | PORNBOX: DORCEL CLUB |
| 4311 | `custom.pornbox-dreamroom` | PORNBOX: DREAMROOM |
| 4313 | `custom.pornbox-exotic` | PORNBOX: EXOTIC |
| 4315 | `custom.pornbox-fake-hostel` | PORNBOX: FAKE HOSTEL |
| 4317 | `custom.pornbox-fake-taxi` | PORNBOX: FAKE TAXI |
| 4319 | `custom.pornbox-family-strokes` | PORNBOX: FAMILY STROKES |
| 4321 | `custom.pornbox-family-swap-xxx` | PORNBOX: FAMILY SWAP XXX |
| 4323 | `custom.pornbox-fapadoo` | PORNBOX: FAPADOO |
| 4325 | `custom.pornbox-filthy-kings` | PORNBOX: FILTHY KINGS |
| 4327 | `custom.pornbox-first-anal-quest` | PORNBOX: FIRST ANAL QUEST |
| 4329 | `custom.pornbox-first-class-pov` | PORNBOX: FIRST CLASS POV |
| 4331 | `custom.pornbox-fit-18` | PORNBOX: FIT 18 |
| 4333 | `custom.pornbox-gangbang-creampie` | PORNBOX: GANGBANG CREAMPIE |
| 4335 | `custom.pornbox-gotmylf` | PORNBOX: GOTMYLF |
| 4337 | `custom.pornbox-hentained` | PORNBOX: HENTAINED |
| 4339 | `custom.pornbox-her-limit` | PORNBOX: HER LIMIT |
| 4341 | `custom.pornbox-holed` | PORNBOX: HOLED |
| 4343 | `custom.pornbox-horny-dream-babez` | PORNBOX: HORNY DREAM BABEZ |
| 4345 | `custom.pornbox-horny-hostel` | PORNBOX: HORNY HOSTEL |
| 4347 | `custom.pornbox-hot-wife-xxx` | PORNBOX: HOT WIFE XXX |
| 4349 | `custom.pornbox-hussie-pass` | PORNBOX: HUSSIE PASS |
| 4351 | `custom.pornbox-interracial-pass` | PORNBOX: INTERRACIAL PASS |
| 4353 | `custom.pornbox-joi-babes` | PORNBOX: JOI BABES |
| 4355 | `custom.pornbox-kinky-family` | PORNBOX: KINKY FAMILY |
| 4357 | `custom.pornbox-kinky-inlaws` | PORNBOX: KINKY INLAWS |
| 4359 | `custom.pornbox-kinky-spa` | PORNBOX: KINKY SPA |
| 4361 | `custom.pornbox-lethal-teens` | PORNBOX: LETHAL TEENS |
| 4363 | `custom.pornbox-lets-doe-it` | PORNBOX: LETS DOE IT |
| 4365 | `custom.pornbox-life-selector` | PORNBOX: LIFE SELECTOR |
| 4367 | `custom.pornbox-love-her-feet` | PORNBOX: LOVE HER FEET |
| 4369 | `custom.pornbox-love-home-porn` | PORNBOX: LOVE HOME PORN |
| 4371 | `custom.pornbox-lubed` | PORNBOX: LUBED |
| 4373 | `custom.pornbox-lw-productions` | PORNBOX: LW PRODUCTIONS |
| 4375 | `custom.pornbox-mamacitaz` | PORNBOX: MAMACITAZ |
| 4377 | `custom.pornbox-mano-job` | PORNBOX: MANO JOB |
| 4379 | `custom.pornbox-massage-rooms` | PORNBOX: MASSAGE ROOMS |
| 4381 | `custom.pornbox-max-j` | PORNBOX: MAX J |
| 4383 | `custom.pornbox-mofos` | PORNBOX: MOFOS |
| 4385 | `custom.pornbox-mom-teach-sex` | PORNBOX: MOM TEACH SEX |
| 4387 | `custom.pornbox-mom-xxx` | PORNBOX: MOM XXX |
| 4389 | `custom.pornbox-my-18-teens` | PORNBOX: MY 18 TEENS |
| 4391 | `custom.pornbox-my-dirty-hobby` | PORNBOX: MY DIRTY HOBBY |
| 4393 | `custom.pornbox-my-family-pies` | PORNBOX: MY FAMILY PIES |
| 4395 | `custom.pornbox-my-life-in-miami` | PORNBOX: MY LIFE IN MIAMI |
| 4397 | `custom.pornbox-my-pervy-family` | PORNBOX: MY PERVY FAMILY |
| 4399 | `custom.pornbox-mylf` | PORNBOX: MYLF |
| 4401 | `custom.pornbox-new-sensations` | PORNBOX: NEW SENSATIONS |
| 4403 | `custom.pornbox-nf-busty` | PORNBOX: NF BUSTY |
| 4405 | `custom.pornbox-nubile-films` | PORNBOX: NUBILE FILMS |
| 4407 | `custom.pornbox-passion` | PORNBOX: PASSION |
| 4409 | `custom.pornbox-perv-city` | PORNBOX: PERV CITY |
| 4411 | `custom.pornbox-perv-mom` | PORNBOX: PERV MOM |
| 4413 | `custom.pornbox-pooksi` | PORNBOX: POOKSI |
| 4415 | `custom.pornbox-porn-world-hardcore` | PORNBOX: PORN WORLD HARDCORE |
| 4417 | `custom.pornbox-pornhochic` | PORNBOX: PORNHOCHIC |
| 4419 | `custom.pornbox-pov-masters` | PORNBOX: POV MASTERS |
| 4421 | `custom.pornbox-private` | PORNBOX: PRIVATE |
| 4423 | `custom.pornbox-private-society` | PORNBOX: PRIVATE SOCIETY |
| 4425 | `custom.pornbox-puba` | PORNBOX: PUBA |
| 4427 | `custom.pornbox-public-agent` | PORNBOX: PUBLIC AGENT |
| 4429 | `custom.pornbox-pure-mature` | PORNBOX: PURE MATURE |
| 4431 | `custom.pornbox-raw-attack` | PORNBOX: RAW ATTACK |
| 4433 | `custom.pornbox-reality-junkies` | PORNBOX: REALITY JUNKIES |
| 4435 | `custom.pornbox-reality-kings` | PORNBOX: REALITY KINGS |
| 4437 | `custom.pornbox-shagging-moms` | PORNBOX: SHAGGING MOMS |
| 4439 | `custom.pornbox-she-is-nerdy` | PORNBOX: SHE IS NERDY |
| 4441 | `custom.pornbox-slim` | PORNBOX: SLIM |
| 4443 | `custom.pornbox-sofie-marie-xxx` | PORNBOX: SOFIE MARIE XXX |
| 4445 | `custom.pornbox-strokies` | PORNBOX: STROKIES |
| 4447 | `custom.pornbox-sugar-babes-tv` | PORNBOX: SUGAR BABES TV |
| 4449 | `custom.pornbox-sweet-sinner` | PORNBOX: SWEET SINNER |
| 4451 | `custom.pornbox-sweetheart-porn` | PORNBOX: SWEETHEART PORN |
| 4453 | `custom.pornbox-the-white-boxxx` | PORNBOX: THE WHITE BOXXX |
| 4455 | `custom.pornbox-true-amateurs` | PORNBOX: TRUE AMATEURS |
| 4457 | `custom.pornbox-twisty` | PORNBOX: TWISTY |
| 4459 | `custom.xxx-pornstar` | Pornstar |
| 4461 | `custom.xxx-pov` | POV |
| 4463 | `custom.xxx-princess-cum` | Princess Cum |
| 4465 | `PureBabes.us` | Pure Babes |
| 4467 | `custom.24-7-xxx-pure-taboo` | Pure Taboo |
| 4469 | `custom.24-7-xxx-rated` | Rated |
| 4471 | `custom.24-7-xxx-rated-3` | Rated 3 |
| 4473 | `custom.xxx-real-wife-stories` | Real Wife Stories |
| 4475 | `custom.24-7-xxx-reality-kings` | Reality Kings |
| 4477 | `custom.xxx-reality-kings` | Reality Kings |
| 4479 | `custom.24-7-xxx-riley-reid` | Riley Reid |
| 4481 | `custom.xxx-rough` | Rough |
| 4483 | `custom.xxx-russian` | Russian |
| 4485 | `custom.xxx-russian-night` | Russian Night |
| 4487 | `custom.xxx-sexto-sento` | Sexto Sento |
| 4489 | `custom.24-7-xxx-shoplyfter` | ShopLyfter |
| 4491 | `custom.stars-exclusive-abella-danger` | STARS EXCLUSIVE: ABELLA DANGER |
| 4493 | `custom.stars-exclusive-adriana-chechik` | STARS EXCLUSIVE: ADRIANA CHECHIK |
| 4495 | `custom.stars-exclusive-alina-lopez` | STARS EXCLUSIVE: ALINA LOPEZ |
| 4497 | `custom.stars-exclusive-angela-white` | STARS EXCLUSIVE: ANGELA WHITE |
| 4499 | `custom.stars-exclusive-ariana-marie` | STARS EXCLUSIVE: ARIANA MARIE |
| 4501 | `custom.stars-exclusive-august-ames` | STARS EXCLUSIVE: AUGUST AMES |
| 4503 | `custom.stars-exclusive-autumn-falls` | STARS EXCLUSIVE: AUTUMN FALLS |
| 4505 | `custom.stars-exclusive-blake-blossom` | STARS EXCLUSIVE: BLAKE BLOSSOM |
| 4507 | `custom.stars-exclusive-brandi-love` | STARS EXCLUSIVE: BRANDI LOVE |
| 4509 | `custom.stars-exclusive-dani-daniels` | STARS EXCLUSIVE: DANI DANIELS |
| 4511 | `custom.stars-exclusive-elsa-jean` | STARS EXCLUSIVE: ELSA JEAN |
| 4513 | `custom.stars-exclusive-emily-willis` | STARS EXCLUSIVE: EMILY WILLIS |
| 4515 | `custom.stars-exclusive-eva-lovia` | STARS EXCLUSIVE: EVA LOVIA |
| 4517 | `custom.stars-exclusive-gina-valentina` | STARS EXCLUSIVE: GINA VALENTINA |
| 4519 | `custom.stars-exclusive-jessa-rhodes` | STARS EXCLUSIVE: JESSA RHODES |
| 4521 | `custom.stars-exclusive-lana-rhoades` | STARS EXCLUSIVE: LANA RHOADES |
| 4523 | `custom.stars-exclusive-lena-paul` | STARS EXCLUSIVE: LENA PAUL |
| 4525 | `custom.stars-exclusive-lisa-ann` | STARS EXCLUSIVE: LISA ANN |
| 4527 | `custom.stars-exclusive-madison-ivy` | STARS EXCLUSIVE: MADISON IVY |
| 4529 | `custom.stars-exclusive-mia-malkova` | STARS EXCLUSIVE: MIA MALKOVA |
| 4531 | `custom.stars-exclusive-nicole-aniston` | STARS EXCLUSIVE: NICOLE ANISTON |
| 4533 | `custom.stars-exclusive-riley-reid` | STARS EXCLUSIVE: RILEY REID |
| 4535 | `custom.stars-exclusive-uma-jolie` | STARS EXCLUSIVE: UMA JOLIE |
| 4537 | `custom.stars-exclusive-valentina-nappi` | STARS EXCLUSIVE: VALENTINA NAPPI |
| 4541 | `custom.24-7-xxx-strap-on` | Strap on |
| 4543 | `custom.xxx-super-one` | Super One |
| 4545 | `custom.24-7-xxx-swallowed` | Swallowed |
| 4547 | `custom.xxx-teen-red-tv` | Teen Red TV |
| 4549 | `custom.xxx-threesome` | Threesome |
| 4551 | `custom.xxx-tiny-4k` | Tiny |
| 4553 | `custom.24-7-xxx-trans` | Trans |
| 4555 | `custom.24-7-xxx-true-anal` | True Anal |
| 4557 | `custom.xxx-true-anal` | True Anal |
| 4559 | `custom.24-7-xxx-uniform` | Uniform |
| 4561 | `custom.verified-amateurs-bigtittygothegg` | VERIFIED AMATEURS: BIGTITTYGOTHEGG |
| 4563 | `custom.verified-amateurs-carlacute` | VERIFIED AMATEURS: CARLACUTE |
| 4565 | `custom.verified-amateurs-cherry-grace` | VERIFIED AMATEURS: CHERRY GRACE |
| 4567 | `custom.verified-amateurs-chessie-rae` | VERIFIED AMATEURS: CHESSIE RAE |
| 4569 | `custom.verified-amateurs-diana-daniels` | VERIFIED AMATEURS: DIANA DANIELS |
| 4571 | `custom.verified-amateurs-ella-kojiro` | VERIFIED AMATEURS: ELLA KOJIRO |
| 4573 | `custom.verified-amateurs-kriss-kiss` | VERIFIED AMATEURS: KRISS KISS |
| 4575 | `custom.verified-amateurs-leah-meow` | VERIFIED AMATEURS: LEAH MEOW |
| 4577 | `custom.verified-amateurs-luxurygirl` | VERIFIED AMATEURS: LUXURYGIRL |
| 4579 | `custom.verified-amateurs-mikanika69` | VERIFIED AMATEURS: MIKANIKA69 |
| 4581 | `custom.verified-amateurs-mini-diva` | VERIFIED AMATEURS: MINI DIVA |
| 4583 | `custom.verified-amateurs-mollyredwolf` | VERIFIED AMATEURS: MOLLYREDWOLF |
| 4585 | `custom.verified-amateurs-nofacegirl` | VERIFIED AMATEURS: NOFACEGIRL |
| 4587 | `custom.verified-amateurs-notsoamateur` | VERIFIED AMATEURS: NOTSOAMATEUR |
| 4589 | `custom.verified-amateurs-nyna-ferragni` | VERIFIED AMATEURS: NYNA FERRAGNI |
| 4591 | `custom.verified-amateurs-pamsnusnu` | VERIFIED AMATEURS: PAMSNUSNU |
| 4593 | `custom.verified-amateurs-purple-bitch` | VERIFIED AMATEURS: PURPLE BITCH |
| 4595 | `custom.verified-amateurs-reislin` | VERIFIED AMATEURS: REISLIN |
| 4597 | `custom.verified-amateurs-secretcrush` | VERIFIED AMATEURS: SECRETCRUSH |
| 4599 | `custom.verified-amateurs-shaiden-rouge` | VERIFIED AMATEURS: SHAIDEN ROUGE |
| 4601 | `custom.verified-amateurs-solazola` | VERIFIED AMATEURS: SOLAZOLA |
| 4603 | `custom.verified-amateurs-tessa-winters` | VERIFIED AMATEURS: TESSA WINTERS |
| 4605 | `custom.verified-amateurs-tinna-angel` | VERIFIED AMATEURS: TINNA ANGEL |
| 4607 | `custom.verified-amateurs-yinyleon` | VERIFIED AMATEURS: YINYLEON |
| 4609 | `custom.24-7-xxx-veronica-avluv` | Veronica Avluv |
| 4611 | `custom.24-7-xxx-violet-myers` | Violet Myers |
| 4613 | `custom.xxx-vivid-red` | Vivid Red |
| 4615 | `VividTVEurope.uk` | Vivid TV Europe |
| 4619 | `custom.xxx-wank-it-now` | Wank It Now |
| 4621 | `custom.xxx-xy-max` | Xy Max |
| 4647 | `AbdulmajeedAbdullah.sa@SD` | Abdulmajeed Abdullah |
| 4763 | `BanglaJagoTV.in` | Bangla Jago TV |
| 4855 | `custom.cinema-ru-movie` | Cinema |
| 4891 | `custom.cooking.channel` | Cooking Channel |
| 4893 | `custom.cooking.channel` | Cooking Channel |
| 4909 | `DanceTVEDMMainstage.ee@SD` | DanceTV EDM Mainstage |
| 4911 | `DanceTVMinimalTech.ee@SD` | DanceTV Minimal Tech |
| 5051 | `custom.evil-angel` | Evil Angel |
| 5137 | `custom.bdix.gopal-bhar-tv` | Gopal Bhar TV |
| 5175 | `custom.id-investigation-discovery` | Id Investigation Discovery |
| 5403 | `NewFlix.ir@SD` | NewFlix |
| 5409 | `custom.nick-jr-east` | Nick Jr East |
| 5453 | `PersianaLatino.fr@SD` | Persiana Latino |
| 5457 | `custom.pink-erotic-2` | Pink Erotic 2 |
| 5459 | `custom.pink-erotic-3` | Pink Erotic 3 |
| 5461 | `custom.pink-erotic-5` | Pink Erotic 5 |
| 5463 | `custom.pink-erotic-7` | Pink Erotic 7 |
| 5465 | `custom.pink-erotic-8` | Pink Erotic 8 |
| 5577 | `SkyCinemaAction.it@SD` | Sky Cinema Action |
| 5579 | `SkyCinemaCollection.it@SD` | Sky Cinema Collection |
| 5581 | `SkyCinemaFamily.it@SD` | Sky Cinema Family |
| 5583 | `SkyCinemaSuspense.it@SD` | Sky Cinema Suspense |
| 5585 | `SkyCinemaUno.it@SD` | Sky Cinema Uno |
| 5743 | `custom.trace-gospel-nigeria-and-east-africa-fr-music` | Trace Gospel Nigeria and East Africa |
| 5745 | `custom.trace-gospel-southern-africa-fr-music` | Trace Gospel Southern Africa |
| 5751 | `travel.us` | Travel Channel East |

## Validation boundary
This audit verifies URL format and repository-path existence. It does not claim that every binary image has been decoded, visually checked, or served successfully over HTTP. Those require a separate image-content/HTTP probe.

## Policy
- Use only repository-owned local logos.
- No relative paths, external hosts, generic placeholders, or guessed channel artwork.
- Preserve authentic, unique logo assets; do not replace valid artwork unnecessarily.

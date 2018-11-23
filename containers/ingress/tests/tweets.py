"""
Samples of Tweets pulled from twitter with various structures that are used for various unit tests.
"""

import arrow

import ingress.elastic as ie

TWEET_PARSE_SAMPLES = [
    (
        {
            'created_at': 'Tue Nov 13 17:06:34 +0000 2018',
            'id': 1062391281500983296,
            'id_str': '1062391281500983296',
            'text':
                'RT @potiarnaigh89: This is @duponline logic.\n\n#Brexit - '
                '@10DowningStreet must stick to and deliver on their '
                'promises\n\n#IrishLanguageAct (pr…',
            'source':
                '<a href="http://twitter.com/download/android" rel="nofollow">'
                'Twitter for Android</a>',
            'truncated': False,
            'in_reply_to_status_id': None,
            'in_reply_to_status_id_str': None,
            'in_reply_to_user_id': None,
            'in_reply_to_user_id_str': None,
            'in_reply_to_screen_name': None,
            'user':
                {
                    'id': 43842243,
                    'id_str': '43842243',
                    'name': 'James McCloskey',
                    'screen_name': 'half98',
                    'location': 'Belfast',
                    'url': None,
                    'description': 'Chun Glóire Dé agus onóir na hEireann!',
                    'translator_type': 'none',
                    'protected': False,
                    'verified': False,
                    'followers_count': 366,
                    'friends_count': 139,
                    'listed_count': 7,
                    'favourites_count': 39667,
                    'statuses_count': 31746,
                    'created_at': 'Mon Jun 01 06:20:46 +0000 2009',
                    'utc_offset': None,
                    'time_zone': None,
                    'geo_enabled': True,
                    'lang': 'en',
                    'contributors_enabled': False,
                    'is_translator': False,
                    'profile_background_color': 'C0DEED',
                    'profile_background_image_url':
                        'http://abs.twimg.com/images/themes/theme1/bg.png',
                    'profile_background_image_url_https':
                        'https://abs.twimg.com/images/themes/theme1/bg.png',
                    'profile_background_tile': False,
                    'profile_link_color': '1DA1F2',
                    'profile_sidebar_border_color': 'C0DEED',
                    'profile_sidebar_fill_color': 'DDEEF6',
                    'profile_text_color': '333333',
                    'profile_use_background_image': True,
                    'profile_image_url':
                        'http://pbs.twimg.com/profile_images/3178290882/'
                        '5f6e48d5921de29b930879fe5262a281_normal.jpeg',
                    'profile_image_url_https':
                        'https://pbs.twimg.com/profile_images/3178290882/'
                        '5f6e48d5921de29b930879fe5262a281_normal.jpeg',
                    'profile_banner_url':
                        'https://pbs.twimg.com/profile_banners/43842243/'
                        '1362478392',
                    'default_profile': True,
                    'default_profile_image': False,
                    'following': None,
                    'follow_request_sent': None,
                    'notifications': None
                },
            'geo': None,
            'coordinates': None,
            'place':
                {
                    "id": "585e878a02085de5",
                    "url": "https://api.twitter.com/1.1/geo/id/585e878a02085de5.json",
                    "place_type": "city",
                    "name": "Beersel",
                    "full_name": "Beersel, Belgi\u00eb",
                    "country_code": "BE",
                    "country": "Belgium",
                    "bounding_box":
                        {
                            "type": "Polygon",
                            "coordinates":
                                [
                                    [
                                        [4.25677,
                                         50.713178],
                                        [4.25677,
                                         50.782274],
                                        [4.355722,
                                         50.782274],
                                        [4.355722,
                                         50.713178]
                                    ]
                                ]
                        },
                    "attributes": {}
                },
            'contributors': None,
            'quoted_status_id': 1062048494859571203,
            'quoted_status_id_str': '1062048494859571203',
            'quoted_status':
                {
                    'created_at': 'Mon Nov 12 18:24:27 +0000 2018',
                    'id': 1062048494859571203,
                    'id_str': '1062048494859571203',
                    'text':
                        '"I hope she reverts to the position of sticking to the'
                        ' pledges she has made and looks for a sensible, '
                        'workable way… https://t.co/jgG2394h5c',
                    'display_text_range': [0,
                                           140],
                    'source':
                        '<a href="http://twitter.com/download/iphone" '
                        'rel="nofollow">Twitter for iPhone</a>',
                    'truncated': True,
                    'in_reply_to_status_id': None,
                    'in_reply_to_status_id_str': None,
                    'in_reply_to_user_id': None,
                    'in_reply_to_user_id_str': None,
                    'in_reply_to_screen_name': None,
                    'user':
                        {
                            'id': 104845115,
                            'id_str': '104845115',
                            'name': 'Nigel Dodds',
                            'screen_name': 'NigelDoddsDUP',
                            'location': 'Northern Ireland',
                            'url': None,
                            'description':
                                'Deputy Leader of the Democratic Unionist Party'
                                ' and Member of Parliament for North Belfast.',
                            'translator_type': 'none',
                            'protected': False,
                            'verified': False,
                            'followers_count': 16325,
                            'friends_count': 200,
                            'listed_count': 405,
                            'favourites_count': 1746,
                            'statuses_count': 3636,
                            'created_at': 'Thu Jan 14 15:41:28 +0000 2010',
                            'utc_offset': None,
                            'time_zone': None,
                            'geo_enabled': True,
                            'lang': 'en',
                            'contributors_enabled': False,
                            'is_translator': False,
                            'profile_background_color': 'C0DEED',
                            'profile_background_image_url':
                                'http://abs.twimg.com/images/themes/theme1/bg.png',
                            'profile_background_image_url_https':
                                'https://abs.twimg.com/images/themes/theme1/bg.png',
                            'profile_background_tile': False,
                            'profile_link_color': '1DA1F2',
                            'profile_sidebar_border_color': 'C0DEED',
                            'profile_sidebar_fill_color': 'DDEEF6',
                            'profile_text_color': '333333',
                            'profile_use_background_image': True,
                            'profile_image_url':
                                'http://pbs.twimg.com/profile_images/'
                                '662422316786319360/pO4Rte0B_normal.jpg',
                            'profile_image_url_https':
                                'https://pbs.twimg.com/profile_images/'
                                '662422316786319360/pO4Rte0B_normal.jpg',
                            'profile_banner_url':
                                'https://pbs.twimg.com/profile_banners/'
                                '104845115/1497091947',
                            'default_profile': True,
                            'default_profile_image': False,
                            'following': None,
                            'follow_request_sent': None,
                            'notifications': None
                        },
                    'geo': None,
                    'coordinates': None,
                    'place':
                        {
                            "id": "75e9a3ae84cb5db1",
                            "url": "https://api.twitter.com/1.1/geo/id/75e9a3ae84cb5db1.json",
                            "place_type": "city",
                            "name": "Warwick",
                            "full_name": "Warwick, England",
                            "country_code": "GB",
                            "country": "United Kingdom",
                            "bounding_box":
                                {
                                    "type": "Polygon",
                                    "coordinates":
                                        [
                                            [
                                                [-1.613875,
                                                 52.261064],
                                                [-1.613875,
                                                 52.299529],
                                                [-1.534617,
                                                 52.299529],
                                                [-1.534617,
                                                 52.261064]
                                            ]
                                        ]
                                },
                            "attributes": {}
                        },
                    'contributors': None,
                    'quoted_status_id': 1062017908304429056,
                    'quoted_status_id_str': '1062017908304429056',
                    'is_quote_status': True,
                    'extended_tweet':
                        {
                            'full_text':
                                '"I hope she reverts to the position of '
                                'sticking to the pledges she has made and looks'
                                ' for a sensible, workable way forward.” '
                                'https://t.co/JREpafOFhM',
                            'display_text_range': [0,
                                                   124],
                            'entities':
                                {
                                    'hashtags': [],
                                    'urls':
                                        [
                                            {
                                                'url': 'https://t.co/JREpafOFhM',
                                                'expanded_url':
                                                    'https://twitter.com/'
                                                    'viewfrmstormont/status/'
                                                    '1062017908304429056',
                                                'display_url': 'twitter.com/viewfrmstormon…',
                                                'indices': [125,
                                                            148]
                                            }
                                        ],
                                    'user_mentions': [],
                                    'symbols': []
                                }
                        },
                    'quote_count': 14,
                    'reply_count': 80,
                    'retweet_count': 92,
                    'favorite_count': 227,
                    'entities':
                        {
                            'hashtags': [],
                            'urls':
                                [
                                    {
                                        'url': 'https://t.co/jgG2394h5c',
                                        'expanded_url':
                                            'https://twitter.com/i/web/status/1062048494859571203',
                                        'display_url': 'twitter.com/i/web/status/1…',
                                        'indices': [116,
                                                    139]
                                    }
                                ],
                            'user_mentions': [],
                            'symbols': []
                        },
                    'favorited': False,
                    'retweeted': False,
                    'possibly_sensitive': False,
                    'filter_level': 'low',
                    'lang': 'en'
                },
            'quoted_status_permalink':
                {
                    'url': 'https://t.co/qZX0aWedNX',
                    'expanded': 'https://twitter.com/nigeldoddsdup/status/1062048494859571203?s=21',
                    'display': 'twitter.com/nigeldoddsdup/…'
                },
            'is_quote_status': True,
            'quote_count': 0,
            'reply_count': 0,
            'retweet_count': 0,
            'favorite_count': 0,
            'entities':
                {
                    'hashtags':
                        [
                            {
                                'text': 'Brexit',
                                'indices': [46,
                                            53]
                            },
                            {
                                'text': 'IrishLanguageAct',
                                'indices': [118,
                                            135]
                            }
                        ],
                    'urls': [],
                    'user_mentions':
                        [
                            {
                                'screen_name': 'potiarnaigh89',
                                'name': 'Padaí Ó Tiarnaigh🅾️',
                                'id': 1104799729,
                                'id_str': '1104799729',
                                'indices': [3,
                                            17]
                            },
                            {
                                'screen_name': 'duponline',
                                'name': 'DUP',
                                'id': 19977542,
                                'id_str': '19977542',
                                'indices': [27,
                                            37]
                            },
                            {
                                'screen_name': '10DowningStreet',
                                'name': 'UK Prime Minister',
                                'id': 14224719,
                                'id_str': '14224719',
                                'indices': [56,
                                            72]
                            }
                        ],
                    'symbols': []
                },
            'favorited': False,
            'retweeted': False,
            'filter_level': 'low',
            'lang': 'en',
            'timestamp_ms': '1542128794442',
            'location':
                {
                    'country': 'United Kingdom',
                    'state': 'Northern Ireland',
                    'county': 'County Antrim',
                    'city': 'Belfast',
                    'id': 449,
                    'latitude': 54.595295,
                    'longitude': -5.934524,
                    'resolution_method': 'profile'
                }
        },
        ie.Tweet(
            id='1062391281500983296',
            created_at='Tue Nov 13 17:06:34 +0000 2018',
            text='RT @potiarnaigh89: This is @duponline logic.\n\n#Brexit -'
            ' @10DowningStreet must stick to and deliver on their promises'
            '\n\n#IrishLanguageAct (pr…',
            truncated=False,
            user=ie.User(
                id=43842243,
                location='Belfast',
                description='Chun Glóire Dé agus onóir na hEireann!',
                geo_enabled=True,
                lang='en',
            ),
            geo=None,
            geotagged=False,
            coordinates=None,
            place=ie.Place(
                id="585e878a02085de5",
                url="https://api.twitter.com/1.1/geo/id/585e878a02085de5.json",
                place_type="city",
                name="Beersel",
                full_name="Beersel, Belgi\u00eb",
                country_code="BE",
                country="Belgium",
                bounding_box={
                    "type": "Polygon",
                    "coordinates":
                        [
                            [
                                [4.25677,
                                 50.713178],
                                [4.25677,
                                 50.782274],
                                [4.355722,
                                 50.782274],
                                [4.355722,
                                 50.713178]
                            ]
                        ]
                },
                attributes={},
            ),
            full_text='"I hope she reverts to the position of sticking to the pledges she'
            ' has made and looks for a sensible, workable way forward.” '
            'https://t.co/JREpafOFhM',
            hashtags=[
                'Brexit',
                'IrishLanguageAct',
            ],
            lang='en',
            timestamp=arrow.get(1542128794442 / 1000).datetime,
            location=ie.Location(
                country='United Kingdom',
                state='Northern Ireland',
                county='County Antrim',
                city='Belfast',
                id=449,
                latitude=54.595295,
                longitude=-5.934524,
                resolution_method='profile',
            ),
        )
    ),
    (
        {
            "created_at": "Thu Nov 22 09:59:59 +0000 2018",
            "id": 1065545420699590656,
            "id_str": "1065545420699590656",
            "text":
                "RT @DPGwyther: This weekend, local activists will be out across "
                "the country campaigning for a #PeoplesVote because they're "
                "#NotBuyingIt whe\u2026",
            "source":
                '<a href="https://about.twitter.com/products/tweetdeck" '
                'rel="nofollow">TweetDeck</a>',
            "truncated": False,
            "in_reply_to_status_id": None,
            "in_reply_to_status_id_str": None,
            "in_reply_to_user_id": None,
            "in_reply_to_user_id_str": None,
            "in_reply_to_screen_name": None,
            "user":
                {
                    "id": 4806808293,
                    "id_str": "4806808293",
                    "name": "InFacts",
                    "screen_name": "InFactsOrg",
                    "location": "London, England",
                    "url": "http://infacts.org",
                    "description":
                        "A journalistic enterprise making the fact-based case against Brexit.",
                    "translator_type": "none",
                    "protected": False,
                    "verified": False,
                    "followers_count": 17926,
                    "friends_count": 5556,
                    "listed_count": 270,
                    "favourites_count": 1051,
                    "statuses_count": 11121,
                    "created_at": "Thu Jan 14 19:13:36 +0000 2016",
                    "utc_offset": None,
                    "time_zone": None,
                    "geo_enabled": False,
                    "lang": "en-gb",
                    "contributors_enabled": False,
                    "is_translator": False,
                    "profile_background_color": "000000",
                    "profile_background_image_url":
                        "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "profile_background_image_url_https":
                        "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "profile_background_tile": False,
                    "profile_link_color": "ABB8C2",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "000000",
                    "profile_text_color": "000000",
                    "profile_use_background_image": False,
                    "profile_image_url":
                        "http://pbs.twimg.com/profile_images/735153398803238912/hsNopRbS_normal.jpg",
                    "profile_image_url_https":
                        "https://pbs.twimg.com/profile_images/735153398803238912/hsNopRbS_normal.jpg",
                    "profile_banner_url":
                        "https://pbs.twimg.com/profile_banners/4806808293/1454693484",
                    "default_profile": False,
                    "default_profile_image": False,
                    "following": None,
                    "follow_request_sent": None,
                    "notifications": None
                },
            "geo": None,
            "coordinates": None,
            "place": None,
            "contributors": None,
            "is_quote_status": False,
            "quote_count": 0,
            "reply_count": 0,
            "retweet_count": 0,
            "favorite_count": 0,
            "entities":
                {
                    "hashtags":
                        [
                            {
                                "text": "PeoplesVote",
                                "indices": [94,
                                            106]
                            },
                            {
                                "text": "NotBuyingIt",
                                "indices": [123,
                                            135]
                            }
                        ],
                    "urls": [],
                    "user_mentions":
                        [
                            {
                                "screen_name": "DPGwyther",
                                "name": "David Gwyther",
                                "id": 885882085629722624,
                                "id_str": "885882085629722624",
                                "indices": [3,
                                            13]
                            }
                        ],
                    "symbols": []
                },
            "favorited": False,
            "retweeted": False,
            "filter_level": "low",
            "lang": "en",
            "timestamp_ms": "1542880799828"
        },
        ie.Tweet(
            id='1065545420699590656',
            created_at='Thu Nov 22 09:59:59 +0000 2018',
            text="RT @DPGwyther: This weekend, local activists will be out "
            "across the country campaigning for a #PeoplesVote because "
            "they're #NotBuyingIt whe\u2026",
            truncated=False,
            user=ie.User(
                id=4806808293,
                location='London, England',
                description='A journalistic enterprise making the fact-based case against Brexit.',
                geo_enabled=False,
                lang='en-gb',
            ),
            geo=None,
            geotagged=True,
            coordinates={
                'lat': 51.506325,
                'lon': -0.127144,
            },
            place=ie.Place(
                id=None,
                url=None,
                place_type=None,
                name=None,
                full_name=None,
                country_code=None,
                country=None,
                bounding_box=None,
                attributes=None,
            ),
            full_text=None,
            hashtags=[
                "PeoplesVote",
                "NotBuyingIt",
            ],
            lang='en',
            timestamp=arrow.get(1542880799828 / 1000).datetime,
            location=ie.Location(
                country='United Kingdom',
                state='London',
                county='London',
                city='London',
                id=449,
                latitude=51.506325,
                longitude=-0.127144,
                resolution_method='profile',
            ),
        )
    )
]

stuff = [
    {
        "created_at": "Thu Nov 22 09:59:59 +0000 2018",
        "id": 1065545417721561089,
        "id_str": "1065545417721561089",
        "text":
            "RT @StewartHosieSNP: In the Chamber for the Fisheries Bill "
            "debate, Michael Gove offering warm words and #Brexit platitutes "
            "but struggling t\u2026",
        "source":
            "<a href=\"http://twitter.com/#!/download/ipad\" rel=\"nofollow\">Twitter for iPad</a>",
        "truncated": False,
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user":
            {
                "id": 20311385,
                "id_str": "20311385",
                "name": "36grit",
                "screen_name": "yawdrah",
                "location": "England, United Kingdom",
                "url": None,
                "description": None,
                "translator_type": "none",
                "protected": False,
                "verified": False,
                "followers_count": 1346,
                "friends_count": 1429,
                "listed_count": 9,
                "favourites_count": 106047,
                "statuses_count": 71478,
                "created_at": "Sat Feb 07 14:20:46 +0000 2009",
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": False,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "profile_background_color": "C0DEED",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_image_url_https":
                    "https://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_tile": False,
                "profile_link_color": "1DA1F2",
                "profile_sidebar_border_color": "C0DEED",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": True,
                "profile_image_url":
                    "http://pbs.twimg.com/profile_images/904712256163860480/v_dVGBp4_normal.jpg",
                "profile_image_url_https":
                    "https://pbs.twimg.com/profile_images/904712256163860480/v_dVGBp4_normal.jpg",
                "default_profile": True,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None
            },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "quote_count": 0,
        "reply_count": 0,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities":
            {
                "hashtags": [{
                    "text": "Brexit",
                    "indices": [104,
                                111]
                }],
                "urls": [],
                "user_mentions":
                    [
                        {
                            "screen_name": "StewartHosieSNP",
                            "name": "Stewart Hosie MP",
                            "id": 219298196,
                            "id_str": "219298196",
                            "indices": [3,
                                        19]
                        }
                    ],
                "symbols": []
            },
        "favorited": False,
        "retweeted": False,
        "filter_level": "low",
        "lang": "en",
        "timestamp_ms": "1542880799118"
    },
    {
        "created_at": "Thu Nov 22 10:00:00 +0000 2018",
        "id": 1065545422201081858,
        "id_str": "1065545422201081858",
        "text":
            "There are 3049 hours until we leave the World's largest trading "
            "bloc. \n\nIt might sound crazy, but own Government ha\u2026 "
            "https://t.co/YbUS9SxxJG",
        "source": '<a href="http://www.google.co.uk" rel="nofollow">'
                  'BrexitBeater Bot</a>',
        "truncated": True,
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user":
            {
                "id": 756513906357575681,
                "id_str": "756513906357575681",
                "name": "Brexit Beater",
                "screen_name": "brexitbeater",
                "location": "UK & Germany",
                "url": "http://www.brexitbeater.co.uk",
                "description":
                    "Helping UK start-ups & SME's #remain in the EU by creating"
                    " a subsidiary in Europe's largest and richest market, "
                    "Germany. Tweets by @globaltwit",
                "translator_type": "none",
                "protected": False,
                "verified": False,
                "followers_count": 873,
                "friends_count": 1857,
                "listed_count": 41,
                "favourites_count": 2433,
                "statuses_count": 8343,
                "created_at": "Fri Jul 22 15:39:05 +0000 2016",
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": False,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_image_url_https":
                    "https://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_tile": False,
                "profile_link_color": "1B95E0",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "000000",
                "profile_text_color": "000000",
                "profile_use_background_image": False,
                "profile_image_url":
                    "http://pbs.twimg.com/profile_images/852533994835070978/g5pbP3ZV_normal.jpg",
                "profile_image_url_https":
                    "https://pbs.twimg.com/profile_images/852533994835070978/g5pbP3ZV_normal.jpg",
                "profile_banner_url":
                    "https://pbs.twimg.com/profile_banners/756513906357575681/1506553615",
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None
            },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "extended_tweet":
            {
                "full_text":
                    "There are 3049 hours until we leave the World's largest "
                    "trading bloc. \n\nIt might sound crazy, but own Government"
                    " has recommended that #UK Companies establ anyone? "
                    "https://t.co/mf3i9hjLFs\n\n#GmbH #Brexit #SingleMarket\n"
                    "https://t.co/5IkaIVETr1",
                "display_text_range": [0,
                                       271],
                "entities":
                    {
                        "hashtags":
                            [
                                {
                                    "text": "UK",
                                    "indices": [134,
                                                137]
                                },
                                {
                                    "text": "GmbH",
                                    "indices": [220,
                                                225]
                                },
                                {
                                    "text": "Brexit",
                                    "indices": [226,
                                                233]
                                },
                                {
                                    "text": "SingleMarket",
                                    "indices": [234,
                                                247]
                                }
                            ],
                        "urls":
                            [
                                {
                                    "url": "https://t.co/mf3i9hjLFs",
                                    "expanded_url": "http://www.BrexitBeater.co.uk",
                                    "display_url": "BrexitBeater.co.uk",
                                    "indices": [195,
                                                218]
                                },
                                {
                                    "url": "https://t.co/5IkaIVETr1",
                                    "expanded_url":
                                        "https://www.independent.co.uk/news/uk/"
                                        "politics/brexit-trade-business-eu-uk-"
                                        "hq-no-deal-industry-europe-a8581431.html",
                                    "display_url": "independent.co.uk/news/uk/politi\u2026",
                                    "indices": [248,
                                                271]
                                }
                            ],
                        "user_mentions": [],
                        "symbols": []
                    }
            },
        "quote_count": 0,
        "reply_count": 0,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities":
            {
                "hashtags": [],
                "urls":
                    [
                        {
                            "url": "https://t.co/YbUS9SxxJG",
                            "expanded_url": "https://twitter.com/i/web/status/1065545422201081858",
                            "display_url": "twitter.com/i/web/status/1\u2026",
                            "indices": [117,
                                        140]
                        }
                    ],
                "user_mentions": [],
                "symbols": []
            },
        "favorited": False,
        "retweeted": False,
        "possibly_sensitive": False,
        "filter_level": "low",
        "lang": "en",
        "timestamp_ms": "1542880800186"
    },
    {
        "created_at": "Thu Nov 22 10:00:00 +0000 2018",
        "id": 1065545422163402752,
        "id_str": "1065545422163402752",
        "text":
            "There are 3049 hours until #Brexit - For a realtime countdown "
            "clock, visit https://t.co/JcXN0M5gFc https://t.co/9XmlJWySIh",
        "source": '<a href="http://www.google.co.uk" rel="nofollow">'
                  'BrexitBeater Bot</a>',
        "truncated": False,
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user":
            {
                "id": 756513906357575681,
                "id_str": "756513906357575681",
                "name": "Brexit Beater",
                "screen_name": "brexitbeater",
                "location": "UK & Germany",
                "url": "http://www.brexitbeater.co.uk",
                "description":
                    "Helping UK start-ups & SME's #remain in the EU by creating"
                    " a subsidiary in Europe's largest and richest market, "
                    "Germany. Tweets by @globaltwit",
                "translator_type": "none",
                "protected": False,
                "verified": False,
                "followers_count": 873,
                "friends_count": 1857,
                "listed_count": 41,
                "favourites_count": 2433,
                "statuses_count": 8343,
                "created_at": "Fri Jul 22 15:39:05 +0000 2016",
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": False,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_image_url_https":
                    "https://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_tile": False,
                "profile_link_color": "1B95E0",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "000000",
                "profile_text_color": "000000",
                "profile_use_background_image": False,
                "profile_image_url":
                    "http://pbs.twimg.com/profile_images/852533994835070978/g5pbP3ZV_normal.jpg",
                "profile_image_url_https":
                    "https://pbs.twimg.com/profile_images/852533994835070978/g5pbP3ZV_normal.jpg",
                "profile_banner_url":
                    "https://pbs.twimg.com/profile_banners/756513906357575681/1506553615",
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None
            },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "quote_count": 0,
        "reply_count": 0,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities":
            {
                "hashtags": [{
                    "text": "Brexit",
                    "indices": [27,
                                34]
                }],
                "urls":
                    [
                        {
                            "url": "https://t.co/JcXN0M5gFc",
                            "expanded_url": "http://www.brexitbeater.co.uk",
                            "display_url": "brexitbeater.co.uk",
                            "indices": [75,
                                        98]
                        },
                        {
                            "url": "https://t.co/9XmlJWySIh",
                            "expanded_url":
                                "http://www.independent.co.uk/news/uk/politics/"
                                "brexit-trade-business-eu-uk-hq-no-deal-"
                                "industry-europe-a8581431.html",
                            "display_url": "independent.co.uk/news/uk/"
                                           "politi\u2026",
                            "indices": [99,
                                        122]
                        }
                    ],
                "user_mentions": [],
                "symbols": []
            },
        "favorited": False,
        "retweeted": False,
        "possibly_sensitive": False,
        "filter_level": "low",
        "lang": "en",
        "timestamp_ms": "1542880800177"
    },
    {
        "created_at": "Thu Nov 22 10:00:00 +0000 2018",
        "id": 1065545422536564738,
        "id_str": "1065545422536564738",
        "text":
            "How will #FTSE100 firms be effected by #Brexit? Business as usual?"
            " #postbrexit  https://t.co/sNewofhb46",
        "source":
            "<a href=\"https://ads-api.twitter.com\" rel=\"nofollow\">Twitter "
            "Ads Composer</a>",
        "truncated": False,
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user":
            {
                "id": 721984894570729472,
                "id_str": "721984894570729472",
                "name": "Nicholls Law",
                "screen_name": "NichollsLaw",
                "location": "Southend-on-Sea",
                "url": "https://www.nichollslaw.co.uk/",
                "description":
                    "Relevant content for those interested in cyber security, "
                    "fraud and UK law. \n\nNicholls Law are specialists in "
                    "Fraud, Litigation and Business Law",
                "translator_type": "none",
                "protected": False,
                "verified": False,
                "followers_count": 725,
                "friends_count": 746,
                "listed_count": 14,
                "favourites_count": 74,
                "statuses_count": 1495,
                "created_at": "Mon Apr 18 08:53:07 +0000 2016",
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": False,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_image_url_https":
                    "https://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_tile": False,
                "profile_link_color": "2E8C7C",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "000000",
                "profile_text_color": "000000",
                "profile_use_background_image": False,
                "profile_image_url":
                    "http://pbs.twimg.com/profile_images/721988884100472832/lhQ23z8x_normal.jpg",
                "profile_image_url_https":
                    "https://pbs.twimg.com/profile_images/721988884100472832/lhQ23z8x_normal.jpg",
                "profile_banner_url":
                    "https://pbs.twimg.com/profile_banners/721984894570729472/1541596823",
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None
            },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "quote_count": 0,
        "reply_count": 0,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities":
            {
                "hashtags":
                    [
                        {
                            "text": "FTSE100",
                            "indices": [9,
                                        17]
                        },
                        {
                            "text": "Brexit",
                            "indices": [39,
                                        46]
                        },
                        {
                            "text": "postbrexit",
                            "indices": [67,
                                        78]
                        }
                    ],
                "urls":
                    [
                        {
                            "url": "https://t.co/sNewofhb46",
                            "expanded_url":
                                "https://www.independent.co.uk/news/business/"
                                "analysis-and-features/brexit-business-"
                                "preparation-impact-theresa-may-cbi-speech-ftse"
                                "-economy-risk-mig",
                            "display_url": "independent.co.uk/news/business/\u2026",
                            "indices": [80,
                                        103]
                        }
                    ],
                "user_mentions": [],
                "symbols": []
            },
        "favorited": False,
        "retweeted": False,
        "possibly_sensitive": False,
        "filter_level": "low",
        "lang": "en",
        "timestamp_ms": "1542880800266"
    },
    {
        "created_at": "Thu Nov 22 10:00:00 +0000 2018",
        "id": 1065545422998028288,
        "id_str": "1065545422998028288",
        "text":
            "#ForexNews\n\n\u201cEconomists forecast that UK #GDP growth will "
            "slow to 0.2% in the final quarter, down from the 0.6% in\u2026 "
            "https://t.co/HTMcvAaZiF",
        "source":
            '<a href="https://about.twitter.com/products/tweetdeck" rel="'
            'nofollow">TweetDeck</a>',
        "truncated": True,
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user":
            {
                "id": 115593944,
                "id_str": "115593944",
                "name": "FXPRIMUS",
                "screen_name": "FXPRIMUS",
                "location": None,
                "url": "https://www.fxprimus.com/int",
                "description":
                    "FXPRIMUS is globally acclaimed for offering one of the "
                    "safest and most secure online trading environments "
                    "available anywhere in the forex industry.",
                "translator_type": "none",
                "protected": False,
                "verified": False,
                "followers_count": 6059,
                "friends_count": 5127,
                "listed_count": 103,
                "favourites_count": 177,
                "statuses_count": 6125,
                "created_at": "Fri Feb 19 06:11:03 +0000 2010",
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": True,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "profile_background_color": "036C9C",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_image_url_https":
                    "https://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_tile": False,
                "profile_link_color": "004B70",
                "profile_sidebar_border_color": "C3CBDE",
                "profile_sidebar_fill_color": "DCEBF5",
                "profile_text_color": "333333",
                "profile_use_background_image": True,
                "profile_image_url":
                    "http://pbs.twimg.com/profile_images/1022829423899357184/Vhw2vJFj_normal.jpg",
                "profile_image_url_https":
                    "https://pbs.twimg.com/profile_images/1022829423899357184/Vhw2vJFj_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/115593944/1533113594",
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None
            },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "extended_tweet":
            {
                "full_text":
                    "#ForexNews\n\n\u201cEconomists forecast that UK #GDP "
                    "growth will slow to 0.2% in the final quarter, down from "
                    "the 0.6% in the previous three months. #Busine t level "
                    "since 2009, according to a survey from IHS Markit.\u201d "
                    "#Brexit \n\nhttps://t.co/R3bEoGCSrW",
                "display_text_range": [0,
                                       276],
                "entities":
                    {
                        "hashtags":
                            [
                                {
                                    "text": "ForexNews",
                                    "indices": [0,
                                                10]
                                },
                                {
                                    "text": "GDP",
                                    "indices": [41,
                                                45]
                                },
                                {
                                    "text": "BusinessOptimism",
                                    "indices": [142,
                                                159]
                                },
                                {
                                    "text": "Brexit",
                                    "indices": [243,
                                                250]
                                }
                            ],
                        "urls":
                            [
                                {
                                    "url": "https://t.co/R3bEoGCSrW",
                                    "expanded_url": "https://gu.com/p/axn3g/stw",
                                    "display_url": "gu.com/p/axn3g/stw",
                                    "indices": [253,
                                                276]
                                }
                            ],
                        "user_mentions": [],
                        "symbols": []
                    }
            },
        "quote_count": 0,
        "reply_count": 0,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities":
            {
                "hashtags":
                    [
                        {
                            "text": "ForexNews",
                            "indices": [0,
                                        10]
                        },
                        {
                            "text": "GDP",
                            "indices": [41,
                                        45]
                        }
                    ],
                "urls":
                    [
                        {
                            "url": "https://t.co/HTMcvAaZiF",
                            "expanded_url": "https://twitter.com/i/web/status/1065545422998028288",
                            "display_url": "twitter.com/i/web/status/1\u2026",
                            "indices": [116,
                                        139]
                        }
                    ],
                "user_mentions": [],
                "symbols": []
            },
        "favorited": False,
        "retweeted": False,
        "possibly_sensitive": False,
        "filter_level": "low",
        "lang": "en",
        "timestamp_ms": "1542880800376"
    },
    {
        "created_at": "Thu Nov 22 10:00:00 +0000 2018",
        "id": 1065545423354585089,
        "id_str": "1065545423354585089",
        "text":
            "#\u0130ngiltere Ba\u015fbakan\u0131 May'den '#Brexit' A\u00e7"
            "\u0131klamas\u0131 https://t.co/F6k9hRyKjb "
            "https://t.co/o1oNKXfagk",
        "display_text_range": [0,
                               73],
        "source":
            '<a href="https://about.twitter.com/products/tweetdeck" rel="'
            'nofollow">TweetDeck</a>',
        "truncated": False,
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user":
            {
                "id": 1346116590,
                "id_str": "1346116590",
                "name": "CRI T\u00fcrk\u00e7e",
                "screen_name": "CRI_Turkish",
                "location": "China Beijing",
                "url": "http://turkish.cri.cn/",
                "description": "Resmi Twitter Hesab\u0131d\u0131r.",
                "translator_type": "none",
                "protected": False,
                "verified": True,
                "followers_count": 81958,
                "friends_count": 46,
                "listed_count": 123,
                "favourites_count": 113,
                "statuses_count": 21958,
                "created_at": "Fri Apr 12 06:21:54 +0000 2013",
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": True,
                "lang": "tr",
                "contributors_enabled": False,
                "is_translator": False,
                "profile_background_color": "C0DEED",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_image_url_https":
                    "https://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_tile": False,
                "profile_link_color": "1DA1F2",
                "profile_sidebar_border_color": "C0DEED",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": True,
                "profile_image_url":
                    "http://pbs.twimg.com/profile_images/950859782465966080/ueUI9TMI_normal.jpg",
                "profile_image_url_https":
                    "https://pbs.twimg.com/profile_images/950859782465966080/ueUI9TMI_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/1346116590/1527167953",
                "default_profile": True,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None
            },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "quote_count": 0,
        "reply_count": 0,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities":
            {
                "hashtags":
                    [
                        {
                            "text": "\u0130ngiltere",
                            "indices": [0,
                                        10]
                        },
                        {
                            "text": "Brexit",
                            "indices": [30,
                                        37]
                        }
                    ],
                "urls":
                    [
                        {
                            "url": "https://t.co/F6k9hRyKjb",
                            "expanded_url": "https://goo.gl/fmtXzH",
                            "display_url": "goo.gl/fmtXzH",
                            "indices": [50,
                                        73]
                        }
                    ],
                "user_mentions": [],
                "symbols": [],
                "media":
                    [
                        {
                            "id": 1065530330944282624,
                            "id_str": "1065530330944282624",
                            "indices": [74,
                                        97],
                            "media_url": "http://pbs.twimg.com/media/DsmGMMlWoAArIFf.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/DsmGMMlWoAArIFf.jpg",
                            "url": "https://t.co/o1oNKXfagk",
                            "display_url": "pic.twitter.com/o1oNKXfagk",
                            "expanded_url":
                                "https://twitter.com/CRI_Turkish/status/"
                                "1065545423354585089/photo/1",
                            "type": "photo",
                            "sizes":
                                {
                                    "thumb": {
                                        "w": 150,
                                        "h": 150,
                                        "resize": "crop"
                                    },
                                    "medium": {
                                        "w": 1194,
                                        "h": 722,
                                        "resize": "fit"
                                    },
                                    "small": {
                                        "w": 680,
                                        "h": 411,
                                        "resize": "fit"
                                    },
                                    "large": {
                                        "w": 1194,
                                        "h": 722,
                                        "resize": "fit"
                                    }
                                }
                        }
                    ]
            },
        "extended_entities":
            {
                "media":
                    [
                        {
                            "id": 1065530330944282624,
                            "id_str": "1065530330944282624",
                            "indices": [74,
                                        97],
                            "media_url": "http://pbs.twimg.com/media/DsmGMMlWoAArIFf.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/DsmGMMlWoAArIFf.jpg",
                            "url": "https://t.co/o1oNKXfagk",
                            "display_url": "pic.twitter.com/o1oNKXfagk",
                            "expanded_url":
                                "https://twitter.com/CRI_Turkish/status/"
                                "1065545423354585089/photo/1",
                            "type": "photo",
                            "sizes":
                                {
                                    "thumb": {
                                        "w": 150,
                                        "h": 150,
                                        "resize": "crop"
                                    },
                                    "medium": {
                                        "w": 1194,
                                        "h": 722,
                                        "resize": "fit"
                                    },
                                    "small": {
                                        "w": 680,
                                        "h": 411,
                                        "resize": "fit"
                                    },
                                    "large": {
                                        "w": 1194,
                                        "h": 722,
                                        "resize": "fit"
                                    }
                                }
                        }
                    ]
            },
        "favorited": False,
        "retweeted": False,
        "possibly_sensitive": False,
        "filter_level": "low",
        "lang": "tr",
        "timestamp_ms": "1542880800461"
    },
    {
        "created_at": "Thu Nov 22 10:00:01 +0000 2018",
        "id": 1065545426756091904,
        "id_str": "1065545426756091904",
        "text":
            "On the same day that a panel session tackled the topic of #Brexit,"
            " Theresa May was about to present the final deal\u2026 https://"
            "t.co/cmzbHw3grw",
        "display_text_range": [0,
                               140],
        "source": "<a href=\"https://www.sprinklr.com\" rel=\"nofollow\">Sprinklr</a>",
        "truncated": True,
        "in_reply_to_status_id": None,
        "in_reply_to_status_id_str": None,
        "in_reply_to_user_id": None,
        "in_reply_to_user_id_str": None,
        "in_reply_to_screen_name": None,
        "user":
            {
                "id": 109262371,
                "id_str": "109262371",
                "name": "SuperReturn",
                "screen_name": "SuperReturn",
                "location": "London, UK",
                "url": "https://goo.gl/fx9tc5",
                "description":
                    "SuperReturn provides the leading #PrivateEquity & "
                    "#VentureCapital events across the globe.  Next up: "
                    "#SuperInvestor 13-16 Nov in #Amsterdam",
                "translator_type": "none",
                "protected": False,
                "verified": False,
                "followers_count": 4328,
                "friends_count": 753,
                "listed_count": 261,
                "favourites_count": 1959,
                "statuses_count": 15111,
                "created_at": "Thu Jan 28 13:39:20 +0000 2010",
                "utc_offset": None,
                "time_zone": None,
                "geo_enabled": True,
                "lang": "en",
                "contributors_enabled": False,
                "is_translator": False,
                "profile_background_color": "022330",
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme15/bg.png",
                "profile_background_image_url_https":
                    "https://abs.twimg.com/images/themes/theme15/bg.png",
                "profile_background_tile": False,
                "profile_link_color": "000088",
                "profile_sidebar_border_color": "FFFFFF",
                "profile_sidebar_fill_color": "C0DFEC",
                "profile_text_color": "333333",
                "profile_use_background_image": False,
                "profile_image_url":
                    "http://pbs.twimg.com/profile_images/835259208874475521/d1rP3wNC_normal.jpg",
                "profile_image_url_https":
                    "https://pbs.twimg.com/profile_images/835259208874475521/d1rP3wNC_normal.jpg",
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/109262371/1527180769",
                "default_profile": False,
                "default_profile_image": False,
                "following": None,
                "follow_request_sent": None,
                "notifications": None
            },
        "geo": None,
        "coordinates": None,
        "place": None,
        "contributors": None,
        "is_quote_status": False,
        "extended_tweet":
            {
                "full_text":
                    "On the same day that a panel session tackled the topic of "
                    "#Brexit, Theresa May was about to present the final deal "
                    "to her ministers. Resignations were widel 5 "
                    "https://t.co/6hdLJc6D2H https://t.co/CBik8mHDmN",
                "display_text_range": [0,
                                       209],
                "entities":
                    {
                        "hashtags": [{
                            "text": "Brexit",
                            "indices": [58,
                                        65]
                        }],
                        "urls":
                            [
                                {
                                    "url": "https://t.co/6hdLJc6D2H",
                                    "expanded_url": "http://spr.ly/6010ED1Zn",
                                    "display_url": "spr.ly/6010ED1Zn",
                                    "indices": [186,
                                                209]
                                }
                            ],
                        "user_mentions": [],
                        "symbols": [],
                        "media":
                            [
                                {
                                    "id": 1065545425221021696,
                                    "id_str": "1065545425221021696",
                                    "indices": [210,
                                                233],
                                    "media_url": "http://pbs.twimg.com/media/DsmT6zJXcAAzg4P.jpg",
                                    "media_url_https":
                                        "https://pbs.twimg.com/media/DsmT6zJXcAAzg4P.jpg",
                                    "url": "https://t.co/CBik8mHDmN",
                                    "display_url": "pic.twitter.com/CBik8mHDmN",
                                    "expanded_url":
                                        "https://twitter.com/SuperReturn/status"
                                        "/1065545426756091904/photo/1",
                                    "type": "photo",
                                    "sizes":
                                        {
                                            "thumb": {
                                                "w": 150,
                                                "h": 150,
                                                "resize": "crop"
                                            },
                                            "medium": {
                                                "w": 720,
                                                "h": 405,
                                                "resize": "fit"
                                            },
                                            "small": {
                                                "w": 680,
                                                "h": 383,
                                                "resize": "fit"
                                            },
                                            "large": {
                                                "w": 720,
                                                "h": 405,
                                                "resize": "fit"
                                            }
                                        }
                                }
                            ]
                    },
                "extended_entities":
                    {
                        "media":
                            [
                                {
                                    "id": 1065545425221021696,
                                    "id_str": "1065545425221021696",
                                    "indices": [210,
                                                233],
                                    "media_url": "http://pbs.twimg.com/media/DsmT6zJXcAAzg4P.jpg",
                                    "media_url_https":
                                        "https://pbs.twimg.com/media/DsmT6zJXcAAzg4P.jpg",
                                    "url": "https://t.co/CBik8mHDmN",
                                    "display_url": "pic.twitter.com/CBik8mHDmN",
                                    "expanded_url":
                                        "https://twitter.com/SuperReturn/status"
                                        "/1065545426756091904/photo/1",
                                    "type": "photo",
                                    "sizes":
                                        {
                                            "thumb": {
                                                "w": 150,
                                                "h": 150,
                                                "resize": "crop"
                                            },
                                            "medium": {
                                                "w": 720,
                                                "h": 405,
                                                "resize": "fit"
                                            },
                                            "small": {
                                                "w": 680,
                                                "h": 383,
                                                "resize": "fit"
                                            },
                                            "large": {
                                                "w": 720,
                                                "h": 405,
                                                "resize": "fit"
                                            }
                                        }
                                }
                            ]
                    }
            },
        "quote_count": 0,
        "reply_count": 0,
        "retweet_count": 0,
        "favorite_count": 0,
        "entities":
            {
                "hashtags": [{
                    "text": "Brexit",
                    "indices": [58,
                                65]
                }],
                "urls":
                    [
                        {
                            "url": "https://t.co/cmzbHw3grw",
                            "expanded_url": "https://twitter.com/i/web/status/1065545426756091904",
                            "display_url": "twitter.com/i/web/status/1\u2026",
                            "indices": [116,
                                        139]
                        }
                    ],
                "user_mentions": [],
                "symbols": []
            },
        "favorited": False,
        "retweeted": False,
        "possibly_sensitive": False,
        "filter_level": "low",
        "lang": "en",
        "timestamp_ms": "1542880801272"
    },
]

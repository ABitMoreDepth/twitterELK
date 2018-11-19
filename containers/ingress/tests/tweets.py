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
                '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',
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
                        'http://pbs.twimg.com/profile_images/3178290882/5f6e48d5921de29b930879fe5262a281_normal.jpeg',
                    'profile_image_url_https':
                        'https://pbs.twimg.com/profile_images/3178290882/5f6e48d5921de29b930879fe5262a281_normal.jpeg',
                    'profile_banner_url':
                        'https://pbs.twimg.com/profile_banners/43842243/1362478392',
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
            'retweeted_status':
                {
                    'created_at': 'Mon Nov 12 21:32:58 +0000 2018',
                    'id': 1062095935600234497,
                    'id_str': '1062095935600234497',
                    'text':
                        'This is @duponline logic.\n\n#Brexit - '
                        '@10DowningStreet must stick to and deliver on their '
                        'promises… https://t.co/GpHu30BEVL',
                    'source':
                        '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
                    'truncated': True,
                    'in_reply_to_status_id': None,
                    'in_reply_to_status_id_str': None,
                    'in_reply_to_user_id': None,
                    'in_reply_to_user_id_str': None,
                    'in_reply_to_screen_name': None,
                    'user':
                        {
                            'id': 1104799729,
                            'id_str': '1104799729',
                            'name': 'Padaí Ó Tiarnaigh🅾️',
                            'screen_name': 'potiarnaigh89',
                            'location': None,
                            'url': None,
                            'description':
                                'Gael Ard Mhacha.Suim ollmhór i dteanga,cultúr '
                                '& cluichí Gaelacha.Liomsa na tuairimí - leatsa'
                                ' na freagraí.Opinions are mine; answers are '
                                'yours.RT not endorsement',
                            'translator_type': 'regular',
                            'protected': False,
                            'verified': False,
                            'followers_count': 1940,
                            'friends_count': 2316,
                            'listed_count': 22,
                            'favourites_count': 8905,
                            'statuses_count': 12303,
                            'created_at': 'Sat Jan 19 22:16:23 +0000 2013',
                            'utc_offset': None,
                            'time_zone': None,
                            'geo_enabled': True,
                            'lang': 'ga',
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
                                'http://pbs.twimg.com/profile_images/1011371706731003906/gpER2pDD_normal.jpg',
                            'profile_image_url_https':
                                'https://pbs.twimg.com/profile_images/1011371706731003906/gpER2pDD_normal.jpg',
                            'profile_banner_url':
                                'https://pbs.twimg.com/profile_banners/1104799729/1430739880',
                            'default_profile': True,
                            'default_profile_image': False,
                            'following': None,
                            'follow_request_sent': None,
                            'notifications': None
                        },
                    'geo': None,
                    'coordinates': None,
                    'place': None,
                    'contributors': None,
                    'quoted_status_id': 1062048494859571203,
                    'quoted_status_id_str': '1062048494859571203',
                    'quoted_status':
                        {
                            'created_at': 'Mon Nov 12 18:24:27 +0000 2018',
                            'id': 1062048494859571203,
                            'id_str': '1062048494859571203',
                            'text':
                                '"I hope she reverts to the position of '
                                'sticking to the pledges she has made and looks'
                                ' for a sensible, workable way… '
                                'https://t.co/jgG2394h5c',
                            'display_text_range': [0,
                                                   140],
                            'source':
                                '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
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
                                        'Deputy Leader of the Democratic '
                                        'Unionist Party and Member of '
                                        'Parliament for North Belfast.',
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
                                        'http://pbs.twimg.com/profile_images/662422316786319360/pO4Rte0B_normal.jpg',
                                    'profile_image_url_https':
                                        'https://pbs.twimg.com/profile_images/662422316786319360/pO4Rte0B_normal.jpg',
                                    'profile_banner_url':
                                        'https://pbs.twimg.com/profile_banners/104845115/1497091947',
                                    'default_profile': True,
                                    'default_profile_image': False,
                                    'following': None,
                                    'follow_request_sent': None,
                                    'notifications': None
                                },
                            'geo': None,
                            'coordinates': None,
                            'place': None,
                            'contributors': None,
                            'quoted_status_id': 1062017908304429056,
                            'quoted_status_id_str': '1062017908304429056',
                            'is_quote_status': True,
                            'extended_tweet':
                                {
                                    'full_text':
                                        '"I hope she reverts to the position of'
                                        ' sticking to the pledges she has made '
                                        'and looks for a sensible, workable way'
                                        ' forward.” https://t.co/JREpafOFhM',
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
                                                            'https://twitter.com/viewfrmstormont/status/1062017908304429056',
                                                        'display_url':
                                                            'twitter.com/viewfrmstormon…',
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
                            'expanded':
                                'https://twitter.com/nigeldoddsdup/status/1062048494859571203?s=21',
                            'display': 'twitter.com/nigeldoddsdup/…'
                        },
                    'is_quote_status': True,
                    'extended_tweet':
                        {
                            'full_text':
                                'This is @duponline logic.\n\n#Brexit - '
                                '@10DowningStreet must stick to and deliver on '
                                'their promises\n\n#IrishLanguageAct (promised '
                                'by @10DowningStreet during 2006 St Andrews) - '
                                '“What promise?”\n\n#Aye  '
                                '\n\nhttps://t.co/qZX0aWedNX',
                            'display_text_range': [0,
                                                   221],
                            'entities':
                                {
                                    'hashtags':
                                        [
                                            {
                                                'text': 'Brexit',
                                                'indices': [27,
                                                            34]
                                            },
                                            {
                                                'text': 'IrishLanguageAct',
                                                'indices': [99,
                                                            116]
                                            },
                                            {
                                                'text': 'Aye',
                                                'indices': [190,
                                                            194]
                                            }
                                        ],
                                    'urls':
                                        [
                                            {
                                                'url': 'https://t.co/qZX0aWedNX',
                                                'expanded_url':
                                                    'https://twitter.com/nigeldoddsdup/status/1062048494859571203?s=21',
                                                'display_url': 'twitter.com/nigeldoddsdup/…',
                                                'indices': [198,
                                                            221]
                                            }
                                        ],
                                    'user_mentions':
                                        [
                                            {
                                                'screen_name': 'duponline',
                                                'name': 'DUP',
                                                'id': 19977542,
                                                'id_str': '19977542',
                                                'indices': [8,
                                                            18]
                                            },
                                            {
                                                'screen_name': '10DowningStreet',
                                                'name': 'UK Prime Minister',
                                                'id': 14224719,
                                                'id_str': '14224719',
                                                'indices': [37,
                                                            53]
                                            },
                                            {
                                                'screen_name': '10DowningStreet',
                                                'name': 'UK Prime Minister',
                                                'id': 14224719,
                                                'id_str': '14224719',
                                                'indices': [130,
                                                            146]
                                            }
                                        ],
                                    'symbols': []
                                }
                        },
                    'quote_count': 0,
                    'reply_count': 1,
                    'retweet_count': 10,
                    'favorite_count': 25,
                    'entities':
                        {
                            'hashtags': [{
                                'text': 'Brexit',
                                'indices': [27,
                                            34]
                            }],
                            'urls':
                                [
                                    {
                                        'url': 'https://t.co/GpHu30BEVL',
                                        'expanded_url':
                                            'https://twitter.com/i/web/status/1062095935600234497',
                                        'display_url': 'twitter.com/i/web/status/1…',
                                        'indices': [99,
                                                    122]
                                    }
                                ],
                            'user_mentions':
                                [
                                    {
                                        'screen_name': 'duponline',
                                        'name': 'DUP',
                                        'id': 19977542,
                                        'id_str': '19977542',
                                        'indices': [8,
                                                    18]
                                    },
                                    {
                                        'screen_name': '10DowningStreet',
                                        'name': 'UK Prime Minister',
                                        'id': 14224719,
                                        'id_str': '14224719',
                                        'indices': [37,
                                                    53]
                                    }
                                ],
                            'symbols': []
                        },
                    'favorited': False,
                    'retweeted': False,
                    'possibly_sensitive': False,
                    'filter_level': 'low',
                    'lang': 'en'
                },
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
                        '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>',
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
                                'http://pbs.twimg.com/profile_images/662422316786319360/pO4Rte0B_normal.jpg',
                            'profile_image_url_https':
                                'https://pbs.twimg.com/profile_images/662422316786319360/pO4Rte0B_normal.jpg',
                            'profile_banner_url':
                                'https://pbs.twimg.com/profile_banners/104845115/1497091947',
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
                                                    'https://twitter.com/viewfrmstormont/status/1062017908304429056',
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
            geotagged=None,
            coordinates=None,
            place=ie.Place(
                id= "585e878a02085de5",
                url= "https://api.twitter.com/1.1/geo/id/585e878a02085de5.json",
                place_type="city",
                name="Beersel",
                full_name= "Beersel, Belgi\u00eb",
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
            hashtags=None,
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
]

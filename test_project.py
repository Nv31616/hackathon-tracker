from project import filter_hack_list,parse_json,extract_build_id
from datetime import datetime
import pytest

def test_filter_hack_list():
    sample_unstop = [
        {
            'name':'Hackathon1',
            'college':'College1',
            'city':'chennai',
            'link':'https://unstop.com/hackathon1',
            'reg_end':datetime.fromisoformat('2024-03-10T14:30:00Z'),
            'end':datetime.fromisoformat('2024-03-16T14:30:00Z'),
            'team_max':'4',
            'team_min':'2'
        },

        {
            'name':"Hackathon2",
            'college':"College2",
            'city':'mumbai',
            'link':'https://unstop.com/hackathon2',
            'reg_end': datetime.fromisoformat('2024-03-16T14:30:00Z'),
            'end': datetime.fromisoformat('2024-03-20T14:30:00Z'),
            'team_max':'6',
            'team_min':'3'            
        },

        {
            'name':"Hackathon3",
            'college':"College3",
            'city':'indore',
            'link':'https://unstop.com/hackathon3',
            'reg_end': datetime.fromisoformat('2024-04-06T14:30:00Z'),
            'end': datetime.fromisoformat('2024-04-15T14:30:00Z'),
            'team_max':'6',
            'team_min':'3'            
        }
    ]

    sample_devfolio = [
        {
            'name':'Ideathon1',
            'team_max':'3',
            'team_min':'1',
            'city':'mumbai',
            'college':'College4',
            'start':datetime.fromisoformat('2026-03-24T04:30:00+00:00'),
            'end':datetime.fromisoformat('2026-03-25T04:30:00+00:00'),
            'reg_end':datetime.fromisoformat('2026-03-13T04:30:00+00:00'),
            'link':'https://ideathon1.devfolio.co/'
        },
        {
            'name':'Ideathon2',
            'team_max':'5',
            'team_min':'2',
            'city':'',
            'college':'College5',
            'start':datetime.fromisoformat('2026-04-28T04:30:00+00:00'),
            'end':datetime.fromisoformat('2026-04-29T04:30:00+00:00'),
            'reg_end':datetime.fromisoformat('2026-04-13T04:30:00+00:00'),
            'link':'https://ideathon2.devfolio.co/'
        },
        {
            'name':'Ideathon3',
            'team_max':'4',
            'team_min':'2',
            'city':'delhi',
            'college':'College6',
            'start':datetime.fromisoformat('2026-05-13T04:30:00+00:00'),
            'end':datetime.fromisoformat('2026-05-15T04:30:00+00:00'),
            'reg_end':datetime.fromisoformat('2026-05-09T04:30:00+00:00'),
            'link':'https://ideathon3.devfolio.co/'
        },
    ]

    assert filter_hack_list(sample_unstop,sample_devfolio,'') == (sample_unstop,sample_devfolio)
    assert filter_hack_list(sample_unstop,sample_devfolio,'mumbai') == ([sample_unstop[1]],[sample_devfolio[0]])
    assert filter_hack_list(sample_unstop,sample_devfolio,"Mumbai") == ([sample_unstop[1]],[sample_devfolio[0]])
    assert filter_hack_list(sample_unstop,sample_devfolio,' CHENNAI ') == ([sample_unstop[0]],[])

def test_parse_json():
    sample_unstop_json = {
        'data': {
            'data': [
                {
                    "public_url": "hackathons/fastathon",
                    "title": "Fastathon",
                    "organisation": {
                        "name": "College1",
                    },
                    "address_with_country_logo": {
                        "id": 1673030,
                        "address": "College1,Chennai",
                        "city": "Chennai",
                        "state": "Tamil Nadu"
                    },
                    "end_date": "2026-03-25T14:00:00+05:30",
                    "regnRequirements": {
                        "opportunity_id": 1652806,
                        "start_regn_dt": "2026-03-05T00:00:00+05:30",
                        "end_regn_dt": "2026-03-19T00:00:00+05:30",
                        "min_team_size": 2,
                        "max_team_size": 4,
                    }
                },

                {
                    "public_url": "hackathons/hacknova",
                    "title": "HackNova",
                    "organisation": {
                        "name": "College2",
                    },
                    "address_with_country_logo": {
                        "id": 1673030,
                        "address": "College2,City2",
                        "city": "City2",
                        "state": "State2"
                    },
                    "end_date": "2026-06-25T14:00:00+05:30",
                    "regnRequirements": {
                        "opportunity_id": 1652806,
                        "start_regn_dt": "2026-06-05T00:00:00+05:30",
                        "end_regn_dt": "2026-06-19T00:00:00+05:30",
                        "min_team_size": 2,
                        "max_team_size": 4,
                    }
                },

                {
                    "public_url": "hackathons/ideathon",
                    "title": "Ideathon",
                    "organisation": {
                        "name": "College3",
                    },
                    "address_with_country_logo": {
                        "id": 1673030,
                        "address": "College3,city3",
                        "city": "city3",
                        "state": "state3"
                    },
                    "end_date": "2027-03-25T14:00:00+05:30",
                    "regnRequirements": {
                        "opportunity_id": 1652806,
                        "start_regn_dt": "2027-03-05T00:00:00+05:30",
                        "end_regn_dt": "2027-03-19T00:00:00+05:30",
                        "min_team_size": 1,
                        "max_team_size": 3,
                    }
                }              
            ]
        }
    }
    sample_devfolio_json = [
        {
            "pageProps": {
                "hackathon": {
                "uuid": "ed8b373fa4844d128ad9df7a56c4c5d5",
                "name": "HACKANOVA 5.O",
                "slug": "hackanova-4-0",
                "team_min": 2,
                "team_max": 4,
                "starts_at": "2026-03-13T04:30:00+00:00",
                "ends_at": "2026-03-14T16:00:00+00:00",
                "city": "Mumbai",
                "country": "India",
                "location": "College1,Mumbai",
                "settings": {
                    "reg_ends_at": "2026-03-10T18:45:00+00:00",
                    "reg_starts_at": "2026-01-28T08:30:00+00:00",
                    }
                }
            }
        },

        {
            "pageProps": {
                "hackathon": {
                "uuid": "ed8b373fa4844d128ad9df7a56c4c5d5",
                "name": "HACKATHON 2.O",
                "slug": "hackathon2-2-0",
                "team_min": 1,
                "team_max": 2,
                "starts_at": "2026-04-13T04:30:00+00:00",
                "ends_at": "2026-04-14T16:00:00+00:00",
                "city": "Chennai",
                "country": "India",
                "location": "College2,Chennai",
                "settings": {
                    "reg_ends_at": "2026-03-31T18:45:00+00:00",
                    "reg_starts_at": "2026-01-28T08:30:00+00:00",
                    }
                }
            }
        },

        {
            "pageProps": {
                "hackathon": {
                "uuid": "ed8b373fa4844d128ad9df7a56c4c5d5",
                "name": "Ideathon 3.0",
                "slug": "ideathon-3-0",
                "team_min": 2,
                "team_max": 6,
                "starts_at": "2026-06-13T04:30:00+00:00",
                "ends_at": "2026-06-14T16:00:00+00:00",
                "city": None,
                "country": "India",
                "location": "College4",
                "settings": {
                    "reg_ends_at": "2026-03-10T18:45:00+00:00",
                    "reg_starts_at": "2026-01-28T08:30:00+00:00",
                    }
                }
            }
        }
    ]

    sample_devfolio = [
            {
                'name':'HACKANOVA 5.O',
                'team_max':4,
                'team_min':2,
                'city':"Mumbai",
                'college':"College1,Mumbai",
                'start':datetime.fromisoformat("2026-03-13T04:30:00+00:00"),
                'end':datetime.fromisoformat("2026-03-14T16:00:00+00:00"),
                'reg_end':datetime.fromisoformat("2026-03-10T18:45:00+00:00"),
                'link':"https://hackanova-4-0.devfolio.co/"
            },

            {
                'name':"HACKATHON 2.O",
                'team_max':2,
                'team_min':1,
                'city':'Chennai',
                'college':"College2,Chennai",
                'start':datetime.fromisoformat("2026-04-13T04:30:00+00:00"),
                'end':datetime.fromisoformat("2026-04-14T16:00:00+00:00"),
                'reg_end':datetime.fromisoformat("2026-03-31T18:45:00+00:00"),
                'link':"https://hackathon2-2-0.devfolio.co/"
            },

            {
                'name':"Ideathon 3.0",
                'team_max':6,
                'team_min':2,
                'city':'',
                'college':"College4",
                'start':datetime.fromisoformat("2026-06-13T04:30:00+00:00"),
                'end':datetime.fromisoformat("2026-06-14T16:00:00+00:00"),
                'reg_end':datetime.fromisoformat("2026-03-10T18:45:00+00:00"),
                'link':"https://ideathon-3-0.devfolio.co/"
            }
    ]
    sample_unstop = [
        {
            'name':"Fastathon",
            'reg_end':datetime.fromisoformat("2026-03-19T00:00:00+05:30"),
            'team_min':2,
            'team_max':4,
            'city':"Chennai",
            'college':"College1",
            'end':datetime.fromisoformat("2026-03-25T14:00:00+05:30"),
            'link':"https://unstop.com/hackathons/fastathon"
        },

        {
            'name':"HackNova",
            'reg_end':datetime.fromisoformat("2026-06-19T00:00:00+05:30"),
            'team_min':2,
            'team_max':4,
            'city':'City2',
            'college':"College2",
            'end':datetime.fromisoformat("2026-06-25T14:00:00+05:30"),
            'link':"https://unstop.com/hackathons/hacknova"
        },

        {
            'name':"Ideathon",
            'reg_end':datetime.fromisoformat("2027-03-19T00:00:00+05:30"),
            'team_min':1,
            'team_max':3,
            'city':"city3",
            'college':"College3",
            'end':datetime.fromisoformat("2027-03-25T14:00:00+05:30"),
            'link':"https://unstop.com/hackathons/ideathon"
        }
    ]

    assert parse_json([sample_unstop_json],sample_devfolio_json) == (sample_unstop,sample_devfolio)

def test_extract_build_id():
    sample_html = "....../_next/static/Cm7123jueICe0djVs1R5L/_buildManifest.js"
    assert extract_build_id(sample_html) == "Cm7123jueICe0djVs1R5L"
    with pytest.raises(ValueError):
        extract_build_id('<html></html>')
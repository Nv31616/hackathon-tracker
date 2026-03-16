from project import filter_hack_list,parse_json
from datetime import datetime

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
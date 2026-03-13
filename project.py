import requests
import time
from datetime import datetime
from tqdm import tqdm
import re

def main():
    build_id = get_build_id()
    total_pages = calculate_pages()

    unstop_json_list,devfolio_json_list = get_data(build_id,total_pages)

    unstop_list, devfolio_list = parse_json(unstop_json_list, devfolio_json_list)

    city = input("Enter the city as filter for hackathons (default=Mumbai)")

    filtered_unstop_list, filtered_devfolio_list = filter_hack_list(unstop_list,devfolio_list,city)

    display_hack_list(filtered_unstop_list,filtered_devfolio_list)

def calculate_pages():
    base_url = "https://unstop.com/api/public/opportunity/search-result?&opportunity=hackathons&per_page=18&oppstatus=open&undefined=true&page="
    total_pages = requests.get(base_url, headers={"User-Agent": "HackathonTracker (Contact: nishantv10092005@gmail.com)"}).json()['data']['last_page']
    return total_pages

def get_build_id():
    url = "https://devfolio.co/hackathons"
    response = requests.get(url,headers={"User-Agent": "HackathonTracker (Contact: nishantv10092005@gmail.com)"})  #HTTP Request
    time.sleep(2) # delay
    html_content = response.text
    pattern = r"\/_next\/static\/([A-Za-z0-9_-]+)\/_buildManifest\.js"
    build_id = re.findall(pattern,html_content)[0]
    return build_id

def get_data(build_id,total_pages):
    base_url = "https://unstop.com/api/public/opportunity/search-result?&opportunity=hackathons&per_page=18&oppstatus=open&undefined=true&page="
    unstop_json_list = []
    for i in tqdm(range(total_pages)):
        response = requests.get(f"{base_url}{i+1}", headers={"User-Agent": "HackathonTracker (Contact: nishantv10092005@gmail.com)"})
        time.sleep(2)
        unstop_json_list.append(response.json())
    
    devfolio_json_list = []
    hack_response = requests.get(f"https://devfolio.co/_next/data/{build_id}/hackathons.json",headers={"User-Agent": "HackathonTracker (Contact: nishantv10092005@gmail.com)"})  #HTTP Request
    time.sleep(2) # delay
    hack_json = hack_response.json()
    list = hack_json['pageProps']['dehydratedState']['queries'][0]['state']['data']['open_hackathons']
    for h in tqdm(list):
        slug = h['slug']
        overview_url = f"https://{slug}.devfolio.co/_next/data/{build_id}/hackathon3/{slug}.devfolio.co/overview.json"
        overview_response = requests.get(overview_url,headers={"User-Agent": "HackathonTracker (Contact: nishantv10092005@gmail.com)"}) #HTTP Request
        time.sleep(2) # delay
        overview_json = overview_response.json()
        devfolio_json_list.append(overview_json)
    
    return unstop_json_list,devfolio_json_list

def parse_json(unstop_json_list,devfolio_json_list):
    unstop_list = []
    for h in unstop_json_list:
        for j in range(len(h['data']['data'])):
            name = h['data']['data'][j]['title']
            link = f"https://unstop.com/{h['data']['data'][j]['public_url']}"
            city = h['data']['data'][j]['address_with_country_logo']['city']
            end_date = datetime.fromisoformat(h['data']['data'][j]['end_date'])
            reg_end = datetime.fromisoformat(h['data']['data'][j]["regnRequirements"]['end_regn_dt'])
            team_min = h['data']['data'][j]["regnRequirements"]['min_team_size']
            team_max = h['data']['data'][j]["regnRequirements"]['max_team_size']
            college = h['data']['data'][j]['organisation']['name']
            unstop_list.append({'name':name,'reg_end':reg_end,'team_min':team_min,'team_max':team_max,'city':city,'college':college,'end':end_date,'link':link})
        
    devfolio_list = []
    try:
        for h in devfolio_json_list:
            name = h['pageProps']['hackathon']['name']
            team_max = h['pageProps']['hackathon']['team_max']
            team_min = h['pageProps']['hackathon']['team_min']
            city = h['pageProps']['hackathon']['city']
            college = h['pageProps']['hackathon']['location']
            start = datetime.fromisoformat(h['pageProps']['hackathon']['starts_at'])
            end = datetime.fromisoformat(h['pageProps']['hackathon']['ends_at'])
            reg_end = datetime.fromisoformat(h['pageProps']['hackathon']['settings']['reg_ends_at'])
            link = f"https://{h['pageProps']['hackathon']['slug']}.devfolio.co/"
            dictionary = {
                'name':name,
                'team_max':team_max,
                'team_min':team_min,
                'city':city,
                'college':college,
                'start':start,
                'end':end,
                'reg_end':reg_end,
                'link':link
            }
            devfolio_list.append(dictionary)
    except:
        pass
        

    return unstop_list,devfolio_list    

def filter_hack_list(unstop_list,devfolio_list,city):
    filtered_unstop_list = []
    for h in unstop_list:
        try:
            if city.lower() == "mumbai":
                filtered_unstop_list.append(h)
        except:
            continue

    filtered_devfolio_list = []
    for h in devfolio_list:
        try:
            if h['city'].lower()=='mumbai':
                filtered_devfolio_list.append(h)
        except:
            pass

    return filtered_unstop_list,filtered_devfolio_list        


def display_hack_list(filtered_unstop_list,filtered_devfolio_list):
    print("---------Unstop---------")
    print(f"Found {len(filtered_unstop_list)} Hackathons !!")
    for h in filtered_unstop_list:
        print(f'🚀 {h['name']}')
        print(f'🎓 Hosted By: {h['college']}')
        reg_end = f"{h['reg_end'].day} {h['reg_end'].strftime('%B')}"
        end = f"{h['end'].day} {h['end'].strftime('%B')}"  # Converting datetime obj to simple string like 3 March
        print(f'📅 Dates: {end}')
        print(f'⏳ Registration Closes: {reg_end}')
        print(f'👥 Team Size: {h['team_min']} - {h['team_max']}')
        print(f'🔗 Register here: {h['link']}')
        print('------------------------------------------')

    print("---------Devfolio---------")
    print(f"Found {len(filtered_devfolio_list)} Hackathon(s)!!")
    if filtered_devfolio_list:
        for h in filtered_devfolio_list:
            print(f'🚀 {h['name']}')
            start = f"{h['start'].day} {h['start'].strftime('%B')}" # Converting datetime obj to simple string like 3 March
            end = f"{h['end'].day} {h['end'].strftime('%B')}"  # Converting datetime obj to simple string like 3 March
            reg_end = f"{h['reg_end'].day} {h['reg_end'].strftime('%B')}"   # Converting datetime obj to simple string like 3 March
            print(f'📅 Dates: {start} to {end}')
            print(f'⏳ Registration Closes: {reg_end}')
            print(f'🎓 Hosted by: {h['college']}')
            print(f'👥 Team Size: {h['team_min']} - {h['team_max']}')
            print(f'🔗 Register here: {h['link']}')
            print('------------------------------------------')
    
    else:
        print("No Hackathons found for Mumbai 😢")

main()
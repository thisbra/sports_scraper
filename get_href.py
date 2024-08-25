import requests
from bs4 import BeautifulSoup
import json

# Step 1: Fetch the webpage
url = 'https://fbref.com/en/comps/24/Serie-A-Stats'  # Replace with the actual URL

response = requests.get(url)

if response.status_code != 200:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the table by its ID
table = soup.find('table', id='results2024241_overall')

if not table:
    print("Table with id 'results2024241_overall' not found.")
    exit()

# Step 4: Extract club data (name, crest img src, href)
clubs_data = []

for row in table.find('tbody').find_all('tr'):
    club_info = {}
    
    # Find the club name cell
    team_cell = row.find('td', {'data-stat': 'team'})
    
    if team_cell:
        # Extract club name
        club_name = team_cell.find('a').text.strip()
        club_info['name'] = club_name
        
        # Extract club crest image src
        img_tag = team_cell.find('img')
        if img_tag and 'src' in img_tag.attrs:
            club_info['crest_src'] = img_tag['src']
        else:
            club_info['crest_src'] = None
        
        # Extract club link href
        club_link = team_cell.find('a')
        if club_link and 'href' in club_link.attrs:
            club_info['href'] = club_link['href']
        else:
            club_info['href'] = None
        
        clubs_data.append(club_info)

# Step 5: Convert the data into JSON and save to a file
with open('clubs_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(clubs_data, json_file, ensure_ascii=False, indent=4)

print("Clubs data has been saved to 'clubs_data.json'.")

"""
Get all tables from a team
"""
import json
import time
from urllib import response
from bs4 import BeautifulSoup

import requests
from json_to_csv import json_to_csv
from table_scraper import extract_table_data

def get_all_tables_from_team(team_href):
    response = requests.get(f'https://fbref.com{team_href}')

    # split the team_href to get the team name
    team_name = team_href.split('/')[-1]

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        exit()

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find all tables that have the class 'stats_table'
    tables = soup.find_all('table', class_='stats_table')

    # Step 4: Print the number of tables found and their ids
    print(f"Found {len(tables)} tables in the page")
    for table in tables:
        print(f"Table id: {table['id']}")
    
    # Step 5: Return list of ids
    return [table['id'] for table in tables]
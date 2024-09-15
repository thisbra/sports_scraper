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

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        exit()

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find all tables that have the class 'stats_table'
    tables = soup.find_all('table', class_='stats_table')

    for table in tables:
        table_id = table['id']
        table_name = table_id.replace('_', '-')

        extract_table_data(
            url=f'https://fbref.com{team_href}',
            table_id=table_id,
            table_name=table_name
        )

        json_to_csv(
            f'{table_name}.json',
            f'{table_name}.csv',
            f'data/{table_id}'
        )

        print(f'{table_id} for {team_href} done')

        time.sleep(10)
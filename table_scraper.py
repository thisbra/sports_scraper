import os
import requests
from bs4 import BeautifulSoup
import json
import csv

def extract_table_data(url: str, table_ids: list[str], team_name: str):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    for table_id in table_ids:
        table = soup.find('table', id=table_id)

        if not table:
            print(f'Table with id {table_id} not found.')
            continue

        # Check if there are two header rows
        t_heads = table.find_all('thead')
        trs = t_heads[0].find_all('tr')

        if len(trs) == 2:
            # If there are two header rows, use the second one
            headers = [th.get_text(strip=True) for th in trs[1].find_all('th')]
            data_rows = table.find_all('tr')[2:]  # Skip both header rows
        else:
            # If there's only one header row, use it
            headers = [th.get_text(strip=True) for th in table.find('tr').find_all('th')]
            data_rows = table.find_all('tr')[1:]  # Skip only the first row

        # Extract rows
        rows = []
        for tr in data_rows:
            row = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
            if row:
                rows.append(row)

        # Create directory if it doesn't exist
        os.makedirs(f'data/{table_id}', exist_ok=True)

        # Save as CSV
        csv_filename = f'data/{table_id}/{team_name}_{table_id}.csv'
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)
            writer.writerows(rows)

        print(f'Table data has been saved to {csv_filename}')

        # Save as JSON
        json_filename = f'data/{table_id}/{team_name}_{table_id}.json'
        json_data = [dict(zip(headers, row)) for row in rows]
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        print(f'Table data has been saved to {json_filename}')
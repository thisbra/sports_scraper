import requests
from bs4 import BeautifulSoup
import json

def extract_table_data(url, table_id, table_name):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        exit()

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find the table by its ID
    table = soup.find('table', id=table_id)

    if not table:
        print(f'Table with id {table_id} not found.')
        exit()

    # print(table.prettify())

    # Step 4: Extract headers
    headers = []
    for th in table.find('thead').find_all('th'):
        header = th.get_text(strip=True)
        headers.append(header)

    # Step 5: Extract rows and convert them into a list of dictionaries
    rows = []
    for tr in table.find('tbody').find_all('tr'):
        row_data = {}
        cells = tr.find_all(['th', 'td'])
        for i, cell in enumerate(cells):
            row_data[headers[i]] = cell.get_text(strip=True)
        rows.append(row_data)

    # Step 6: Convert the data into JSON and save to a file
    with open(f'assets/{table_name}.json', 'w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=4)

    print(f'Table data has been saved to assets/{table_name}.json.')

import json

def extract_serie_a(soup):
    table_id = 'results2024241_overall'
    table = soup.find('table', id=table_id)


    if not table:
        print(f'Table with id {table_id} not found.')
        exit()

    

    # Step 4: Extract headers
    headers = []
    for th in table.find('thead').find_all('th'):
        header = th.get_text(strip=True)
        headers.append(header)

    # Step 5: Extract rows and convert them into a list of dictionaries
    rows = []
    # print table rows number
    print(len(table.find('tbody').find_all('tr')))
    for tr in table.find('tbody').find_all('tr'):
        row_data = {}
        cells = tr.find_all(['th', 'td'])
        for i, cell in enumerate(cells):
            row_data[headers[i]] = cell.get_text(strip=True)
        rows.append(row_data)

    # Step 6: Convert the data into JSON and save to a file
    with open('serie_a.json', 'w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=4)

    print(f'Table data has been saved to serie_a.json.')
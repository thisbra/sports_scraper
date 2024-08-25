import json
from json_to_csv import json_to_csv
from table_scraper import extract_table_data

# # Lista da serie A
# extract_table_data(
#     url='https://fbref.com/en/comps/24/Serie-A-Stats',
#     table_id='results2024241_overall',
#     table_name='serie_a'
# )

# # Converter json to csv
# json_to_csv('serie_a.json', 'serie_a.csv')


# Ação para todos os clubes da Série A
with open('assets/clubs_data.json', 'r') as f:
    clubs_data = json.load(f)

    # For each club make array of href
    for club in clubs_data:
        extract_table_data(
            url=f'https://fbref.com/{club["href"]}',
            table_id='matchlogs_for',
            table_name=club['name']
        )

        json_to_csv(f'{club["name"]}.json', f'{club["name"]}.csv')

        print(f'{club["name"]} done')
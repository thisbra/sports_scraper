import json
import time
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

# INSERIR ID DA TABELA AQUI'
table_id = 'stats_standard_24'

# Ação para todos os clubes da Série A
with open('assets/clubs_data.json', 'r') as f:
    clubs_data = json.load(f)

    # For each club make array of href
    for club in clubs_data:
        url = f'https://fbref.com{club["href"]}'
        extract_table_data(
            url=url,
            table_id=table_id,
            table_name=f'{club["name"]}_{table_id}'
        )

        json_to_csv(
            f'{club["name"]}_{table_id}.json',
            f'{club["name"]}_{table_id}.csv',
            f'data/{table_id}'
        )

        print(f'{table_id} for {club["name"]} done')

        time.sleep(10)
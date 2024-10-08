import json
import time
from get_all_tables_from_team import get_all_tables_from_team
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

# # INSERIR ID DA TABELA AQUI'
# table_id = 'stats_standard_24'

# Ação para todos os clubes da Série A
with open('assets/clubs_data.json', 'r') as f:
    table_ids = get_all_tables_from_team('/en/squads/422bb734/Atletico-Mineiro-Stats')

    print(table_ids)

    time.sleep(10)

    clubs_data = json.load(f)

    # For each club make array of href
    for club in clubs_data:
        url = f'https://fbref.com{club["href"]}'

        extract_table_data(
            url=url,
            table_ids=table_ids,
            team_name=url.split('/')[-1]
        )

        print(f'{table_ids} for {club["name"]} done')

        # print missing clubs
        print(f'Missing clubs: {len(clubs_data) - clubs_data.index(club)}')

        time.sleep(15)


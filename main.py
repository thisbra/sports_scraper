# import requests
# from bs4 import BeautifulSoup
# from extract_serie_a import extract_serie_a
# from matchlogs import extract_matchlogs

# url = 'https://fbref.com/en/squads/d9fdd9d9/Botafogo-RJ-Stats'
# response = requests.get(url)
# if response.status_code != 200:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
#     exit()
# soup = BeautifulSoup(response.text, 'html.parser')

# extract_matchlogs(soup)
# extract_serie_a(soup)

from scraper import extract_table_data

# Lista da serie A
extract_table_data(
    url='https://fbref.com/en/comps/24/Serie-A-Stats',
    table_id='results2024241_overall',
    table_name='serie_a'
)


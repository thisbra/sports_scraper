from table_scraper import extract_table_data

# Lista da serie A
extract_table_data(
    url='https://fbref.com/en/comps/24/Serie-A-Stats',
    table_id='results2024241_overall',
    table_name='serie_a'
)


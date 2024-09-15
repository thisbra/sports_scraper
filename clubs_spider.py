import json
from pathlib import Path

import scrapy

class ClubsSpider(scrapy.Spider):
    name = 'clubs'

    def start_requests(self):
        with open('assets/clubs_data.json', 'r') as f:
            clubs_data = json.load(f)
            urls = [f'https://fbref.com{club["href"]}' for club in clubs_data]
            print(urls)
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table_id = 'stats_standard_24'
        club_name = response.url.split('/')[-1]
        club_name = club_name.replace('-', '_')
        table_name = f'{club_name}_{table_id}'
        print(f'Club name: {club_name}')
        print(f'Table name: {table_name}')

        # Save the response body to a file
        Path('data').mkdir(parents=True, exist_ok=True)
        with open(f'data/{table_name}.html', 'wb') as f:
            f.write(response.body)

        print(f'{table_id} for {club_name} done')
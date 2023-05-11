import logging

import bs4
import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')

class Client:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User - Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1 .15(KHTML, like Gecko) Version/15.6.1 Safari/605.1.15'
        }

    def load_page(self, page:int = None):
        url = 'https://www.wildberries.ru/catalog/aksessuary/aksessuary-dlya-volos'
        res = self.session.get(url=url)
        res.raise_for_status()
        return res.text

    def parse_page(self, text:str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('product-card product-card--hoverable j-card-item product-card--adv')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        logger.info(block)
        logger.info('=' * 100)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)


if __name__ == '__main__':
    parser = Client()
    parser.run()
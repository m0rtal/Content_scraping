import scrapy

from .loaders import GCarticleLoader
from .xpath_selectors import PAGINATION, ARTICLES, PAYWALL_ARTICLE_DATA
from ..db_api import Database
from ..tor_browser import TorBrowser


class GirlschaseSpider(scrapy.Spider):
    name = 'girlschase'
    allowed_domains = ['www.girlschase.com', "girlschase.com"]
    start_urls = ['https://www.girlschase.com/articles/all/']
    db = Database(name)

    def _get_follow(self, response, xpath, callback):
        for url in response.xpath(xpath):
            if not self.db.find('url', response.urljoin(url.extract())):  # если ссылки нет в базе
                yield response.follow(url, callback=callback)

    def parse(self, response):
        for item in (PAGINATION, ARTICLES):
            yield from self._get_follow(response, item["selector"], getattr(self, item["callback"]))

    def parse_article(self, response):
        loader = GCarticleLoader(response=response)
        browser = TorBrowser()
        browser.load_page(response.url)
        for key, item in PAYWALL_ARTICLE_DATA.items():
            value = [el.text if key != "images" else el.get_attribute("src") for el in
                     browser.find_elements_by_xpath(item)]
            loader.add_value(key, value)
        data = loader.load_item()
        yield data
        browser.close()

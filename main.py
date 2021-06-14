from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from contenter.spiders.girlschase import GirlschaseSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule("contenter.settings")
    crawler_process = CrawlerProcess(settings=crawler_settings)
    crawler_process.crawl(GirlschaseSpider)
    crawler_process.start()

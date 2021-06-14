import scrapy


class GirlschaseSpider(scrapy.Spider):
    name = 'girlschase'
    allowed_domains = ['www.girlschase.com', "girlschase.com"]
    start_urls = ['https://www.girlschase.com/articles/all/']



    def parse(self, response):
        pass

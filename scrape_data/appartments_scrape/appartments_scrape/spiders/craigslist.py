import scrapy


class CraigslistSpider(scrapy.Spider):
    name = "craigslist"
    allowed_domains = ["dallas.craigslist.org"]
    start_urls = ["https://dallas.craigslist.org/search/apa#search=1~gallery~0~0"]

    def parse(self, response):
        pass


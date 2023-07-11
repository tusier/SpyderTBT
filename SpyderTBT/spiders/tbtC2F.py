import scrapy


class Tbtc2fSpider(scrapy.Spider):
    name = "tbtC2F"
    allowed_domains = ["www.tbt-sps.gov.cn"]
    start_urls = ["http://www.tbt-sps.gov.cn/"]

    def parse(self, response):
        pass

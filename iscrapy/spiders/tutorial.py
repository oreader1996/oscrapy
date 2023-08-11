import scrapy


class TutorialSpider(scrapy.Spider):
    name = "tutorial"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):
        self.logger.info(response.status)
        pass

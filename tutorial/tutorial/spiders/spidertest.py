import scrapy
from tutorial.items import SephoraItem

class SephoraSpider(scrapy.Spider):

    name = "sephorasp"

    def start_requests(self):
        yield scrapy.Request(url = "https://www.sephora.ae/en/stores/", callback = self.parse_pages)

    def parse_pages(self, response):
        for link in response.xpath('//ul[@class="nav-primary"]//a[contains(@class,"level0")]/@href').extract():
            yield scrapy.Request(url = link, callback = self.parse_inner_pages)

    def parse_inner_pages(self, response):
        for links in response.xpath('//li[contains(@class,"amshopby-cat")]/a/@href').extract():
            yield scrapy.Request(url = links, callback = self.target_page)

    def target_page(self, response):
        for titles in response.xpath('//div[@class="product-info"]'):
            product = titles.xpath('.//div[contains(@class,"product-name")]/a/text()').extract_first()
            rate = titles.xpath('.//span[@class="price"]/text()').extract_first()
            yield {'name': product, 'price': rate}

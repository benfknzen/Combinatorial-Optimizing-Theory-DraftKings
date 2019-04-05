import scrapy
# from tutorial.items import TutorialItem


class QuotesSpider(scrapy.Spider):
    name = "secondspider"
    allowed_domains = ['www.superdatascience.com']
    start_urls = [
        'http://www.superdatascience.com/',
    ]

    def parse(self, response):
        item = TutorialItem()
        item['main_headline']=response.xpath('//span/text()').extract()
        item['headline']=response.xpath('//title/tet()').extract()
        item['url']=response.url
        item['project']=self.settings.get('BOT_NAME')
        item['spider']=self.name
        return item

        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }
        #
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

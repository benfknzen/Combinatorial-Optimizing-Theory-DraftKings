import scrapy
from tutorial.items import MovieItem


class imdbSpider(scrapy.Spider):
    name = 'imdbspider'
    allowed_domains = ['imdb.com']
    start_urls = {
        'http://www.imdb.com/chart/top'
    }

    def parse(self, response):
        links = response.xpath('//tbody[@class="lister-list"]/tr/td[@class="titleColumn"]/a/@href').extract()
        i = 1
        for link in links:
            abs_url = response.urljoin(link)
            # url_next = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[' + str[i] + ']/td[2]/a'
            #
            # rating = response.xpath(url_next).extract
            if i <= len(links):
                i = i + 1
            yield scrapy.Request(abs_url, callback=self.parse_indetail, meta={'rating': link})

    def parse_indetail(self, response):
        item = MovieItem()
        item['title'] = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/h1/text()').extract()
        item['directors'] = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a/text()').extract()
        item['writers'] = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[3]/a[1]/text()').extract()
        item['stars'] = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[4]/a[1]/text()').extract()
        item['popularity'] = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/a/span/text()').extract()
        return item

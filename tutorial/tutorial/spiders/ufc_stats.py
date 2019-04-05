import scrapy
from tutorial.items import UfcStats
from scrapy.loader import ItemLoader

class UfcScrape(scrapy.Spider):
    name = "thirdspiderold"
    # allowed_domains = ['ufcstats.com']
    # response.css('a::attr(href)').getall()
    # links to dive into:  links = response.xpath('//a[contains(@href, "fighter-details")]/@href').extract()
    start_urls = [
        'http://ufcstats.com/event-details/9649d75defe0dedb',
        'http://ufcstats.com/event-details/2d5fbe2103f97053',
        # 'http://ufcstats.com/event-details/e96d8538d3f9d0ed',
        # 'http://ufcstats.com/event-details/80eacd4da0617c57',
        # 'http://ufcstats.com/event-details/487c170da059857d',
    ]

    def parse(self, response):

        fighter_list = response.xpath('//a[contains(@href, "fighter-details")]/text()').getall()
        num_fighters = len(fighter_list)
        links = response.xpath('//a[contains(@href, "fighter-details")]/@href').extract()
        i = 0
        for link in links:
            j = int((i+2) / 2)

            if i % 2 == 0:
                scrap_fighter_name = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[2]/p[1]/a/text())'
                scrap_strikes = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[3]/p[1]/text())'
                scrap_takedowns = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[4]/p[1]/text())'
                scrap_submission_attempts = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[5]/p[1]/text())'
                scrap_passes = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[6]/p[1]/text())'
                scrap_weight_class = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[7]/p/text())'
                scrap_method = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[8]/p[1]/text())'
                scrap_round = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[9]/p/text())'
                scrap_time = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[10]/p/text())'
                scrap_result = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[2]/p[1]/a/text())'

            elif i % 2 == 1:
                scrap_fighter_name = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[2]/p[2]/a/text())'
                scrap_strikes = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[3]/p[2]/text())'
                scrap_takedowns = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[4]/p[2]/text())'
                scrap_submission_attempts = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[5]/p[2]/text())'
                scrap_passes = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[6]/p[2]/text())'
                scrap_weight_class = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[7]/p/text())'
                scrap_method = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[8]/p[2]/text())'
                scrap_round = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[9]/p/text())'
                scrap_time = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[10]/p/text())'
                scrap_result = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[2]/p[1]/a/text())'
                # scrapy_results = 'normalize-space(/html/body/section/div/div/table/tbody/tr[' + str(j) + ']/td[1]/p/a/i/i/text())'

            # request = scrapy.Request(url=links[i], callback=self.parse_indetail)

            l = ItemLoader(item=UfcStats(), selector=link)
            l.add_xpath('Fighter_Name', scrap_fighter_name)
            # l.add_xpath('Strikes', scrap_strikes)
            # l.add_xpath('', scrap_)
            i += 1

            yield l.load_item()

            # test = {
            #     # dynamic items
            #     'Fighter_Name': response.xpath(scrap_fighter_name).getall(),
            #     'Strikes': response.xpath(scrap_strikes).getall(),
            #     'Takedowns': response.xpath(scrap_takedowns).getall(),
            #     'Submission_Attempts': response.xpath(scrap_submission_attempts).getall(),
            #     'Passes': response.xpath(scrap_passes).getall(),
            #     'Weight_Class': response.xpath(scrap_weight_class).getall(),
            #     'Method': response.xpath(scrap_method).getall(),
            #     'Round': response.xpath(scrap_round).getall(),
            #     'Time': response.xpath(scrap_time).getall(),
            #     'Result': response.xpath(scrap_result).getall(),
            # 
            #     # static items
            #     'Date': response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()')[1].getall(),
            #     'Location': response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()')[1].getall(),
            #     'Event_Name': response.xpath('normalize-space(/html/body/section/div/h2/span/text())').getall(),
            #     'Height': 'tall_test',
            #     'a': '1', 'b': '2'
            # 
            # }
            # # one = {'asdfas': '1', 'bfadfasfs': '2'}
            # # test.append(one)
            # # a = {'Height': item}
            # # test2 = dict(test.items()+ request.items()) does not work properly, needs to be implemented
            # 
            # yield test



    def parse_indetail(self, response):

        item = UfcStats()
        item['Height'] = response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()').getall()[1]
        item['Weight'] = response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()').getall()[1]
        item['Reach'] = response.xpath('/html/body/section/div/div/div[1]/ul/li[3]/text()').getall()[1]
        item['Stance'] = response.xpath('/html/body/section/div/div/div[1]/ul/li[4]/text()').getall()[1]
        item['DOB'] = response.xpath('/html/body/section/div/div/div[1]/ul/li[5]/text()').getall()[1]
        item['Strikes_Per_Min'] = response.xpath('/html/body/section/div/div/div[2]/div[1]/div[1]/ul/li[1]/text()').getall()[1]
        item['TD_Avg'] = response.xpath('/html/body/section/div/div/div[2]/div[1]/div[2]/ul/li[2]/text()').getall()[1]
        # item = response.meta['item']

        return item

        # yield {
        #     #dynamic items
        #     'Height': response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()').getall()[1],
        # }


#
    # def parse(self, response):
    #     for row in response.xpath('//*[@class="table table-striped"]//tbody/tr'):
    #         yield {
    #             'first' : row.xpath('td[1]//text()').extract_first(),
    #             'last': row.xpath('td[2]//text()').extract_first(),
    #             'handle' : row.xpath('td[3]//text()').extract_first(),
    #         }
    # def parse(self, response):
    #     items = UfcStats()
    #     items['Fighter_Name'] = len(fighter_list)
    #
    #     return items

    # def parse(self, response):
    #     global count
    #     count = 3
    #     items = UfcStats()
    #     items['Fighter_Name']=response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[2]/p[1]/a/text())').getall()
    #     items['Strikes']=response.xpathb    ('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[3]/p[1]/text())').getall()
    #     items['Takedowns']=response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[4]/p[1]/text())').getall()
    #     items['Submission_Attempts']=response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[5]/p[1]/text())').getall()
    #     items['Passes']=response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[6]/p[1]/text())').getall()
    #     items['Weight_Class']=response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[7]/p/text())').getall()
    #     items['Method'] = response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[8]/p[1]/text())').getall()
    #     items['Round'] = response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[9]/p/text())').getall()
    #     items['Time'] = response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[10]/p/text())').getall()
    #     items['Result'] = response.xpath('normalize-space(/html/body/section/div/div/table/tbody/tr[1]/td[1]/p/a/i/i/text())').getall()
    #
    #     # static items
    #     # Date and Location currently have \n and spaces for now 3.27.2019
    #     date = response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()')[1].getall()
    #     date = str(date)
    #     # date = date.re.split(r'\W+', date)
    #     items['Date'] = date
    #
    #     items['Location'] = response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()')[1].getall()
    #
    #
    #     items['Event_Name'] = response.xpath('normalize-space(/html/body/section/div/h2/span/text())').getall()
    #     # if count != 1:
    #     #     count -= 1
    #     #     self.parse(response)
    #
    #     return items

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

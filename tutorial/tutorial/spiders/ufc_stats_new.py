import scrapy
from tutorial.items import UfcStats
from scrapy.loader import ItemLoader

class UfcScrape(scrapy.Spider):
    name = "thirdspider"
    # allowed_domains = ['ufcstats.com']  Giving me a lot of issues 3.30.2019
    # response.css('a::attr(href)').getall()
    # links to dive into:  links = response.xpath('//a[contains(@href, "fighter-details")]/@href').extract()
    start_urls = [
        'http://ufcstats.com/event-details/b0550072e5f0afa7',
    ]

    def parse(self, response):
        links = response.xpath('//a[contains(@href, "fighter-details")]/@href').extract()
        fighters = response.xpath('//a[@class="b-link b-link_style_black"]')
        i = 0
        for fighter in fighters:
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

            # l = ItemLoader(item=UfcStats(), selector=fighter)
            # l.add_xpath('Fighter_Name', './/text()')
            # l.add_xpath('Strikes', '/html/body/section/div/div/table/tbody/tr[1]/td[3]/p[' + str(i+1) + ']')

            if links[i] is not None:
                item1 = UfcStats()
                item2 = {
                    # dynamic items
                    'Fighter_Name': response.xpath(scrap_fighter_name).getall(),
                    'Strikes': response.xpath(scrap_strikes).getall(),
                    'Takedowns': response.xpath(scrap_takedowns).getall(),
                    'Submission_Attempts': response.xpath(scrap_submission_attempts).getall(),
                    'Passes': response.xpath(scrap_passes).getall(),
                    'Weight_Class': response.xpath(scrap_weight_class).getall(),
                    'Method': response.xpath(scrap_method).getall(),
                    'Round': response.xpath(scrap_round).getall(),
                    'Time': response.xpath(scrap_time).getall(),
                    'Result': response.xpath(scrap_result).getall(),

                    # static items
                    'Date': response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()')[1].getall(),
                    'Location': response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()')[1].getall(),
                    'Event_Name': response.xpath('normalize-space(/html/body/section/div/h2/span/text())').getall(),
                }

                item3 = scrapy.Request(url=links[i], callback=self.parse_indetail, meta=item2)

                yield item3

                # for x in test.meta:
                #     l.add_xpath(x, test.meta[x])
            # l.add_xpath(test)
            # yield l.load_item()
            i += 1
        # for link in links:
        #     yield scrapy.Request(url=link, callback=self.parse_indetail)

    def parse_indetail(self, response):
        item = UfcStats()

        # load meta data first
        item['Submission_Attempts'] = response.meta['Submission_Attempts']
        item['Passes'] = response.meta['Passes']
        item['Fighter_Name'] = response.meta['Fighter_Name']
        item['Strikes'] = response.meta['Strikes']
        item['Takedowns'] = response.meta['Takedowns']
        item['Weight_Class'] = response.meta['Weight_Class']
        item['Method'] = response.meta['Method']
        item['Round'] = response.meta['Round']
        item['Time'] = response.meta['Time']
        item['Result'] = response.meta['Result']
        item['Date'] = str(response.meta['Date']).strip().replace('\n', '')
        item['Location'] = str(response.meta['Location']).strip().replace('\n', '')
        item['Event_Name'] = response.meta['Event_Name']

        # Passing data relevant to the new response page
        item['Height'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')
        item['Weight'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()').getall()[1]).strip().replace('\n', '')
        item['Reach'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[3]/text()').getall()[1]).strip().replace('\n', '')
        item['Stance'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[4]/text()').getall()[1]).strip().replace('\n', '')
        item['DOB'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[5]/text()').getall()[1]).strip().replace('\n', '')
        item['Strikes_Per_Min'] = str(response.xpath('/html/body/section/div/div/div[2]/div[1]/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')
        item['TD_Avg'] = str(response.xpath('/html/body/section/div/div/div[2]/div[1]/div[2]/ul/li[2]/text()').getall()[1]).strip().replace('\n', '')
        # # # # item = response.meta['item']
        # #
        return item



import scrapy
from tutorial.items import UfcStats
from scrapy.loader import ItemLoader

class UfcScrape(scrapy.Spider):
    name = "thirdspiderold7.18.2019"
    # allowed_domains = ['ufcstats.com']  Giving me a lot of issues 3.30.2019
    # response.css('a::attr(href)').getall()
    # links to dive into:  links = response.xpath('//a[contains(@href, "fighter-details")]/@href').extract()

    start_urls = ['http://ufcstats.com/event-details/e5d03e4d966126bd']

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

            if links[i] is not None:
                item1 = UfcStats()
                item2 = {
                    # dynamic items
                    'Fighter_Name1': response.xpath(scrap_fighter_name).getall(),
                    # 'Strikes1': response.xpath(scrap_strikes).getall(),
                    # 'Takedowns1': response.xpath(scrap_takedowns).getall(),
                    # 'Submission_Attempts1': response.xpath(scrap_submission_attempts).getall(),
                    # 'Passes1': response.xpath(scrap_passes).getall(),
                    # 'Weight_Class1': response.xpath(scrap_weight_class).getall(),
                    # 'Method1': response.xpath(scrap_method).getall(),
                    # 'Round1': response.xpath(scrap_round).getall(),
                    # 'Time1': response.xpath(scrap_time).getall(),
                    # 'Result1': response.xpath(scrap_result).getall(),

                    # static items
                    'Date': response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()')[1].getall(),
                    'Location': response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()')[1].getall(),
                    'Event_Name': response.xpath('normalize-space(/html/body/section/div/h2/span/text())').getall(),
                }

                item3 = scrapy.Request(url=links[i], callback=self.parse_indetail, meta=item2)

                yield item3

            i += 1


    def parse_indetail(self, response):
        item = UfcStats()

        # load meta data first
        # item['Submission_Attempts1'] = response.meta['Submission_Attempts1']
        # item['Passes1'] = response.meta['Passes1']
        item['Fighter_Name1'] = response.meta['Fighter_Name1']
        # item['Strikes1'] = response.meta['Strikes1']
        # item['Takedowns1'] = response.meta['Takedowns1']
        # item['Weight_Class1'] = response.meta['Weight_Class1']
        # item['Method1'] = response.meta['Method1']
        # item['Round1'] = response.meta['Round1']
        # item['Time1'] = response.meta['Time1']
        # item['Result1'] = response.meta['Result1']
        item['Date'] = str(response.meta['Date']).strip().replace('\n', '')
        item['Location'] = str(response.meta['Location']).strip().replace('\n', '')
        item['Event_Name'] = response.meta['Event_Name']

        # Passing data relevant to the new response page
        item['Height1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')
        item['Weight1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[2]/text()').getall()[1]).strip().replace('\n', '')
        item['Reach1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[3]/text()').getall()[1]).strip().replace('\n', '')
        item['Stance1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[4]/text()').getall()[1]).strip().replace('\n', '')
        item['DOB1'] = str(response.xpath('/html/body/section/div/div/div[1]/ul/li[5]/text()').getall()[1]).strip().replace('\n', '')
        item['Strikes_Per_Min1'] = str(response.xpath('/html/body/section/div/div/div[2]/div[1]/div[1]/ul/li[1]/text()').getall()[1]).strip().replace('\n', '')
        item['TD_Avg1'] = str(response.xpath('/html/body/section/div/div/div[2]/div[1]/div[2]/ul/li[2]/text()').getall()[1]).strip().replace('\n', '')
        # # # # item = response.meta['item']
        # #
        return item



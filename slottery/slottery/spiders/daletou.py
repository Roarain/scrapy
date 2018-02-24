# -*- coding: utf-8 -*-
import scrapy
import sys
import datetime
from decimal import Decimal
from slottery.items import SlotteryItem
from scrapy.http import FormRequest, Request

reload(sys)
sys.setdefaultencoding('utf-8')

class DaletouSpider(scrapy.Spider):
    name = 'daletou'
    allowed_domains = ['datachart.500.com']
    start_urls = ['http://datachart.500.com/dlt/history/newinc/history.php?start=00000&end=99999']

    def parse(self, response):
        node_list = response.xpath("//tbody[@id='tdata']/tr[@class='t_tr1']")
        items = []
        for node in node_list:
            item = SlotteryItem()

            lottery_number = node.xpath("./td[1]/text()").extract()
            front_1 = node.xpath("./td[2]/text()").extract()
            front_2 = node.xpath("./td[3]/text()").extract()
            front_3 = node.xpath("./td[4]/text()").extract()
            front_4 = node.xpath("./td[5]/text()").extract()
            front_5 = node.xpath("./td[6]/text()").extract()
            back_1 = node.xpath("./td[7]/text()").extract()
            back_2 = node.xpath("./td[8]/text()").extract()
            prize_pool_bonus = node.xpath("./td[9]/text()").extract()
            first_prize_count = node.xpath("./td[10]/text()").extract()
            first_prize_bonus = node.xpath("./td[11]/text()").extract()
            second_prize_count = node.xpath("./td[12]/text()").extract()
            second_prize_bonus = node.xpath("./td[13]/text()").extract()
            total_betting_amount = node.xpath("./td[14]/text()").extract()
            lottery_date = node.xpath("./td[15]/text()").extract()

            item['lottery_number'] = lottery_number[0].encode('utf-8')
            item['front_1'] = front_1[0].encode('utf-8')
            item['front_2'] = front_2[0].encode('utf-8')
            item['front_3'] = front_3[0].encode('utf-8')
            item['front_4'] = front_4[0].encode('utf-8')
            item['front_5'] = front_5[0].encode('utf-8')
            item['back_1'] = back_1[0].encode('utf-8')
            item['back_2'] = back_2[0].encode('utf-8')
            item['prize_pool_bonus'] = prize_pool_bonus[0].replace(',', '').encode('utf-8')
            item['first_prize_count'] = first_prize_count[0].encode('utf-8')
            item['first_prize_bonus'] = first_prize_bonus[0].replace(',', '').encode('utf-8')
            item['second_prize_count'] = second_prize_count[0].encode('utf-8')
            item['second_prize_bonus'] = second_prize_bonus[0].replace(',', '').encode('utf-8')
            item['total_betting_amount'] = total_betting_amount[0].replace(',', '').encode('utf-8')
            item['lottery_date'] = lottery_date[0].encode('utf-8')

            items.append(item)

            yield item

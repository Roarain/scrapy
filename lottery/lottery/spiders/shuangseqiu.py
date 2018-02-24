# -*- coding: utf-8 -*-
import scrapy
import sys
import datetime
from decimal import Decimal
from lottery.items import LotteryItem
from scrapy.http import FormRequest, Request


reload(sys)
sys.setdefaultencoding('utf-8')


class ShuangseqiuSpider(scrapy.Spider):
    name = 'shuangseqiu'
    allowed_domains = ['datachart.500.com']
    # start_urls = ['http://datachart.500.com/ssq/history/newinc/history.php?start=03001&end=18020']
    start_urls = ['http://datachart.500.com/ssq/history/newinc/history.php?start=00001&end=99999']

    def parse(self, response):
        node_list = response.xpath("//tr[@class='t_tr1']")
        items = []
        for node in node_list:
            item = LotteryItem()

            lottery_number = node.xpath("./td[1]/text()").extract()
            red_1 = node.xpath("./td[2]/text()").extract()
            red_2 = node.xpath("./td[3]/text()").extract()
            red_3 = node.xpath("./td[4]/text()").extract()
            red_4 = node.xpath("./td[5]/text()").extract()
            red_5 = node.xpath("./td[6]/text()").extract()
            red_6 = node.xpath("./td[7]/text()").extract()
            blue_1 = node.xpath("./td[8]/text()").extract()
            happy_sunday = node.xpath("./td[9]/text()").extract()
            prize_pool_bonus = node.xpath("./td[10]/text()").extract()
            first_prize_count = node.xpath("./td[11]/text()").extract()
            first_prize_bonus = node.xpath("./td[12]/text()").extract()
            second_prize_count = node.xpath("./td[13]/text()").extract()
            second_prize_bonus = node.xpath("./td[14]/text()").extract()
            total_betting_amount = node.xpath("./td[15]/text()").extract()
            lottery_date = node.xpath("./td[16]/text()").extract()

            item['lottery_number'] = lottery_number[0].encode('utf-8')
            item['red_1'] = red_1[0].encode('utf-8')
            item['red_2'] = red_2[0].encode('utf-8')
            item['red_3'] = red_3[0].encode('utf-8')
            item['red_4'] = red_4[0].encode('utf-8')
            item['red_5'] = red_5[0].encode('utf-8')
            item['red_6'] = red_6[0].encode('utf-8')
            item['blue_1'] = blue_1[0].encode('utf-8')
            item['happy_sunday'] = happy_sunday[0].encode('utf-8')
            item['prize_pool_bonus'] = prize_pool_bonus[0].replace(',', '').encode('utf-8')
            item['first_prize_count'] = first_prize_count[0].encode('utf-8')
            item['first_prize_bonus'] = first_prize_bonus[0].replace(',', '').encode('utf-8')
            item['second_prize_count'] = second_prize_count[0].encode('utf-8')
            item['second_prize_bonus'] = second_prize_bonus[0].replace(',', '').encode('utf-8')
            item['total_betting_amount'] = total_betting_amount[0].replace(',', '').encode('utf-8')
            item['lottery_date'] = lottery_date[0].encode('utf-8')
            items.append(item)

            yield item
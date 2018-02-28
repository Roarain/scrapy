# -*- coding: utf-8 -*-
import scrapy
import sys
import datetime
from decimal import Decimal
from clo.items import CloItem
from scrapy.http import FormRequest, Request


reload(sys)
sys.setdefaultencoding('utf-8')


class ZfzxSpider(scrapy.Spider):
    name = 'zfzx'
    allowed_domains = ['zfzx.clo.com.cn']
    # start_urls = ['https://zfzx.clo.com.cn/logout.do']

    def __init__(self, day_number=1, *args, **kwargs):
        super(ZfzxSpider, self).__init__(*args, **kwargs)
        self.form_data_login = {
            'loginName': 'jinf',
            'password': 'jinf',
            'x': '16',
            'y': '6',
            'R1': 'V4'
        }

        self.headers_search_sales_statistics = {
            'Accept': 'image/gif, image/jxr, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, application/x-mfe-ipt, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://zfzx.clo.com.cn/reporting/main.do',
        }

        # 获得今天的日期
        self.today = datetime.date.today()
        # DAY_NUMBER = 2
        # 间隔一天
        self.oneday = datetime.timedelta(days=int(day_number))
        # 获取昨天的日期
        self.yesterday = self.today - self.oneday
        self.yesterday_str = str(self.yesterday)
        self.form_data_search_sales_statistics = {
            # 'end_date': '2017-12-28',
            'end_date': self.yesterday_str,
            'jikai': '所有玩法',
            'report': '销售统计表',
            # 辽宁省的编号是：m6bnb00
            # 'SelectArea': 'm6bnb00',
            # 全国的编号是：d00b00b00
            'SelectArea': 'd00b00b00',
            'setdate': '2017-12-28%2C2017-12-28',
            # 'start_date': '2017-12-28',
            'start_date': self.yesterday_str,
            'thisDate': '5',
        }

    def start_requests(self):
        return [Request(url="https://zfzx.clo.com.cn/logout.do", callback=self.post_login)]

    def post_login(self, response):
        return [FormRequest.from_response(
            response,
            formdata=self.form_data_login,
            callback=self.url_jump,
        )]

    def url_jump(self, response):
        return [Request(url="https://zfzx.clo.com.cn/reporting/main.do", callback=self.search_sales_statistics)]

    def search_sales_statistics(self, response):
        return [FormRequest.from_response(
            response,
            headers=response.request.headers,
            formdata=self.form_data_search_sales_statistics,
            callback=self.parse,
        )]

    def parse(self, response):
        # print response.body.decode("utf-8").encode("gbk")
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item = CloItem()

            hall_name = node.xpath("./td[2]/text()").extract()
            game_lhdb = node.xpath("./td[8]/text()").extract()
            game_xywc = node.xpath("./td[4]/text()").extract()
            game_kxyk = node.xpath("./td[5]/text()").extract()
            game_shxw = node.xpath("./td[6]/text()").extract()
            game_sjfg = node.xpath("./td[7]/text()").extract()
            game_hysj = node.xpath("./td[9]/text()").extract()
            game_qwgef = node.xpath("./td[10]/text()").extract()
            daily_turnover = node.xpath("./td[3]/text()").extract()

            # item['hall_name'] = hall_name[0].encode('utf-8')
            item['hall_name'] = hall_name[0].encode('utf-8')
            item['game_lhdb'] = game_lhdb[0].encode('utf-8')
            item['game_xywc'] = game_xywc[0].encode('utf-8')
            item['game_kxyk'] = game_kxyk[0].encode('utf-8')
            item['game_shxw'] = game_shxw[0].encode('utf-8')
            item['game_sjfg'] = game_sjfg[0].encode('utf-8')
            item['game_hysj'] = game_hysj[0].encode('utf-8')
            item['game_qwgef'] = game_qwgef[0].encode('utf-8')
            item['daily_turnover'] = daily_turnover[0].encode('utf-8')
            item['date_time'] = self.yesterday_str

            yield item
# -*- coding: utf-8 -*-
import scrapy
import sys
from ..items import OpmItem
import re
import time
from scrapy.http import FormRequest, Request
from hall_infos import hall_infos
import logging
import copy
from scrapy.utils.request import request_fingerprint

logging.basicConfig(filename='terminal.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

reload(sys)
sys.setdefaultencoding('utf-8')


class TerminalSpider(scrapy.Spider):

    name = 'terminal'
    allowed_domains = ['114.242.119.194']

    def __init__(self, *args, **kwargs):
        super(TerminalSpider, self).__init__(*args, **kwargs)
        self.counter = {}
        self.giveup = []
        self.hall_infos = copy.deepcopy(hall_infos)
        self.temp_hall_infos = copy.deepcopy(hall_infos)
        self.parameter_name = ('proId', 'areaId', 'hallId')
        self.form_data_login = {
            'referer': 'index.php',
            'login': 'xxx',
            'cookietime': '25920000',
            'password': 'xxx',
            'submit': '马上登陆',
        }

    def start_requests(self):
        return [Request(url="http://114.242.119.194:9714/test.html", callback=self.post_login)]

    def post_login(self, response):
        return [FormRequest.from_response(
            response,
            headers=response.request.headers,
            formdata=self.form_data_login,
            callback=self.post_search_data,
        )]

    def post_search_data(self, response):
        for hall_info in self.hall_infos:
            post_data = dict(zip(self.parameter_name, hall_info))
            yield FormRequest(
                url='http://114.242.119.194:9714/infoplatform/hall/loadPrePareProData.action',
                formdata=post_data,
                callback=self.parse,
                meta=post_data,
                dont_filter=True,
            )

    def parse(self, response):
        node_list = response.xpath("//tr[@bgcolor='#FFFFFF']")
        post_data = {k: v for k, v in response.meta.items() if k in self.parameter_name}
        post_data_hallId = post_data['hallId']

        if not node_list:
            logging.info('parse error post data: {}'.format(post_data))
            if post_data_hallId not in self.counter.keys():
                self.counter[post_data_hallId] = 1
            if self.counter[post_data_hallId] > 30:
                logging.info('give up get data: {}'.format(post_data_hallId))
                return
            elif 0 < self.counter[post_data_hallId] < 30:
                self.counter[post_data_hallId] += 1
                logging.info('{} repeat times: {}'.format(post_data_hallId, self.counter[post_data_hallId]))
                time.sleep(5)
                yield FormRequest(
                    url='http://114.242.119.194:9714/infoplatform/hall/loadPrePareProData.action',
                    formdata=post_data,
                    callback=self.parse,
                    meta=post_data,
                    dont_filter=True,
                )
        else:
            logging.info('parse post data: {}'.format(post_data))
            for node in node_list:
                item = OpmItem()
                proId = post_data['proId']
                areaId = post_data['areaId']
                hallId = post_data['hallId']
                proName = node.xpath("//select[@id='proId']/option[@selected='selected']/text()").extract()
                if proName:
                    proName = proName[0].encode('utf-8')
                else:
                    proName = ''
                areaName = node.xpath("//select[@id='areaId']/option[@selected='selected']/text()").extract()
                if areaName:
                    areaName = areaName[0].encode('utf-8')
                else:
                    areaName = ''
                hallName = node.xpath("//select[@id='hallId']/option[@selected='selected']/text()").extract()
                if hallName:
                    hallName = hallName[0].encode('utf-8')
                else:
                    hallName = ''

                terminal_id = node.xpath("./td[2]/strong/text()").extract()
                terminal_sale = node.xpath("./td[3]/text()").extract()
                terminal_sale_percent = node.xpath("./td[4]/text()").extract()
                terminal_winning = node.xpath("./td[5]/text()").extract()
                terminal_redemption_percent = node.xpath("./td[6]/text()").extract()
                terminal_single_bet = node.xpath("./td[7]/text()").extract()

                item['proId'] = proId
                item['areaId'] = areaId
                item['hallId'] = hallId
                item['proName'] = proName
                item['areaName'] = areaName
                item['hallName'] = hallName
                item['terminal_id'] = terminal_id[0].encode('utf-8').replace('\t', '').replace(' ', '')
                item['terminal_sale'] = terminal_sale[0].encode('utf-8').replace('\t', '').replace(' ', '')
                item['terminal_sale_percent'] = terminal_sale_percent[0].encode('utf-8').replace('\t', '').replace(' ', '')
                item['terminal_winning'] = terminal_winning[0].encode('utf-8').replace('\t', '').replace(' ', '')
                item['terminal_redemption_percent'] = terminal_redemption_percent[0].encode('utf-8').replace('\t', '').replace(' ', '')
                item['terminal_single_bet'] = terminal_single_bet[0].encode('utf-8').replace('\t', '').replace(' ', '')

                logging.info('item data: {}'.format(item))
                yield item
            '''
            if self.temp_hall_infos:
                hall_info = self.temp_hall_infos.pop()
                post_data = dict(zip(self.parameter_name, hall_info))
                yield FormRequest(
                    url='http://114.242.119.194:9714/infoplatform/hall/loadPrePareProData.action',
                    formdata=post_data,
                    callback=self.parse,
                    meta=post_data,
                )
            '''
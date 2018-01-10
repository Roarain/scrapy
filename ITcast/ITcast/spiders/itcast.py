# -*- coding: utf-8 -*-

import scrapy
from ITcast.items import ItcastItem
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class ItcastSpider(scrapy.Spider):
    # 爬虫名称，必须参数
    name = 'itcast'
    # 域的范围，可选参数
    allowed_domains = ['itcast.cn']
    # 起始的url列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # print response.body
        node_list = response.xpath("//div[@class='li_txt']")
        items = []

        for node in node_list:
            item = ItcastItem()

            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)

        return items
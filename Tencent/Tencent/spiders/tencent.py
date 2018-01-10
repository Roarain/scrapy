# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    base_url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            item = TencentItem()

            position_name = node.xpath("./td[1]/a/text()").extract()
            position_link = node.xpath("./td[1]/a/@href").extract()
            position_type = node.xpath("./td[2]/text()").extract()
            people_number = node.xpath("./td[3]/text()").extract()
            work_location = node.xpath("./td[4]/text()").extract()
            publish_time = node.xpath("./td[5]/text()").extract()

            item['position_name'] = position_name[0].encode('utf-8')
            item['position_link'] = position_link[0].encode('utf-8')
            if position_type:
                item['position_type'] = position_type[0].encode('utf-8')
            else:
                item['position_type'] = ''
            item['people_number'] = people_number[0].encode('utf-8')
            item['work_location'] = work_location[0].encode('utf-8')
            item['publish_time'] = publish_time[0].encode('utf-8')

            yield item

        if not response.xpath("//a[@class='noactive' and @id='next']"):
            position_base_url = response.xpath("//*[@id='next']/@href").extract()[0].encode('utf-8')
            url = 'http://hr.tencent.com/' + position_base_url
            yield scrapy.Request(url, callback=self.parse,dont_filter=False)


'''
    # 根据offset来确定总的页数，不能改变
    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        # 从页面获取职位总数
        total_number = int(response.xpath("//div[@class='left']/span/text()").extract()[0])
        print '-' * 20
        print total_number
        print type(total_number)
        print '-' * 20

        for node in node_list:
            item = TencentItem()

            position_name = node.xpath("./td[1]/a/text()").extract()
            position_link = node.xpath("./td[1]/a/@href").extract()
            position_type = node.xpath("./td[2]/text()").extract()
            people_number = node.xpath("./td[3]/text()").extract()
            work_location = node.xpath("./td[4]/text()").extract()
            publish_time = node.xpath("./td[5]/text()").extract()

            item['position_name'] = position_name[0].encode('utf-8')
            item['position_link'] = position_link[0].encode('utf-8')
            if position_type:
                item['position_type'] = position_type[0].encode('utf-8')
            else:
                item['position_type'] = ''
            item['people_number'] = people_number[0].encode('utf-8')
            item['work_location'] = work_location[0].encode('utf-8')
            item['publish_time'] = publish_time[0].encode('utf-8')

            yield item

        if self.offset < total_number:
            self.offset += 10
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)
'''



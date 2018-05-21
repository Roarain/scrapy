# -*- coding: utf-8 -*-
import scrapy
import sys
import datetime
from decimal import Decimal
from mga.items import MgaItem
from scrapy.http import FormRequest, Request


reload(sys)
sys.setdefaultencoding('utf-8')


class LicenseSpider(scrapy.Spider):
    name = 'license'
    allowed_domains = ['searchintegration.mga.org.mt']
    start_urls = ['https://searchintegration.mga.org.mt/Results.aspx?Licencee=&Class=&Status=Licensed&URL=']
    params = (
        ('Licencee', ''),
        ('Class', ''),
        ('Status', 'Licensed'),
        ('URL', ''),
    )

    def parse(self, response):
        node_list = response.xpath("//div[@class='card-details']")
        items = []

        for node in node_list:
            item = MgaItem()

            company_name = node.xpath("./h5/text()").extract()
            reg_no = node.xpath("./div[@class='table']/div[1]/div[2]/text()").extract()
            license_number = node.xpath("./div[@class='table']/div[2]/div[2]/text()").extract()
            license_class = node.xpath("./div[@class='table']/div[3]/div[2]/text()").extract()
            platform = node.xpath("./div[@class='table']/div[4]/div[2]/text()").extract()
            status = node.xpath("./div[@class='table more-details']/div[1]/div[2]/text()").extract()
            registered_address = node.xpath("./div[@class='table more-details']/div[2]/div[2]/text()").extract()
            termination_date = node.xpath("./div[@class='table more-details']/div[3]/div[2]/text()").extract()
            entity_telephone_number = node.xpath("./div[@class='table more-details']/div[4]/div[2]/text()").extract()
            general_email_address = node.xpath("./div[@class='table more-details']/div[6]/div[2]/text()").extract()

            item['company_name'] = company_name[0].encode('utf-8')
            item['reg_no'] = reg_no[0].encode('utf-8')
            item['license_number'] = license_number[0].encode('utf-8')
            item['license_class'] = license_class[0].encode('utf-8')
            item['platform'] = platform[0].encode('utf-8')
            item['status'] = status[0].encode('utf-8')
            item['registered_address'] = registered_address[0].encode('utf-8')
            item['termination_date'] = termination_date[0].encode('utf-8')
            item['entity_telephone_number'] = entity_telephone_number[0].encode('utf-8')
            item['general_email_address'] = general_email_address[0].encode('utf-8')

            items.append(item)

            yield item

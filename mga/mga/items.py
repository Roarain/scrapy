# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MgaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    reg_no = scrapy.Field()
    license_number = scrapy.Field()
    license_class = scrapy.Field()
    platform = scrapy.Field()
    status = scrapy.Field()
    registered_address = scrapy.Field()
    termination_date= scrapy.Field()
    entity_telephone_number = scrapy.Field()
    general_email_address = scrapy.Field()


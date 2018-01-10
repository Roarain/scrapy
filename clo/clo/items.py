# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CloItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hall_name = scrapy.Field()
    game_lhdb = scrapy.Field()
    game_xywc = scrapy.Field()
    game_kxyk = scrapy.Field()
    game_shxw = scrapy.Field()
    game_sjfg = scrapy.Field()
    game_hysj = scrapy.Field()
    game_qwgef = scrapy.Field()
    daily_turnover = scrapy.Field()
    date_time = scrapy.Field()

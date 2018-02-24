# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SlotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lottery_number = scrapy.Field()
    front_1 = scrapy.Field()
    front_2 = scrapy.Field()
    front_3 = scrapy.Field()
    front_4 = scrapy.Field()
    front_5 = scrapy.Field()
    back_1 = scrapy.Field()
    back_2 = scrapy.Field()
    prize_pool_bonus = scrapy.Field()
    first_prize_count = scrapy.Field()
    first_prize_bonus = scrapy.Field()
    second_prize_count = scrapy.Field()
    second_prize_bonus = scrapy.Field()
    total_betting_amount = scrapy.Field()
    lottery_date = scrapy.Field()

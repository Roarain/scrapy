# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LotteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    lottery_number = scrapy.Field()
    red_1 = scrapy.Field()
    red_2 = scrapy.Field()
    red_3 = scrapy.Field()
    red_4 = scrapy.Field()
    red_5 = scrapy.Field()
    red_6 = scrapy.Field()
    blue_1 = scrapy.Field()
    happy_sunday = scrapy.Field()
    prize_pool_bonus = scrapy.Field()
    first_prize_count = scrapy.Field()
    first_prize_bonus = scrapy.Field()
    second_prize_count = scrapy.Field()
    second_prize_bonus = scrapy.Field()
    total_betting_amount = scrapy.Field()
    lottery_date = scrapy.Field()
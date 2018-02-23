# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import MySQLdb
import logging

# 将items返回到cmd终端
# class LotteryPipeline(object):
#     def process_item(self, item, spider):
#         return item


# 将item保存到mysql
class LotteryPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='abcd1234', host='127.0.0.1', port=3306, db='webapp', use_unicode=True, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into shuangseqiu_history(lottery_number, red_1, red_2, red_3, red_4, red_5, red_6, blue_1, happy_sunday, prize_pool_bonus, first_prize_count, first_prize_bonus, second_prize_count, second_prize_bonus, total_betting_amount, lottery_date) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (dict(item)['lottery_number'], dict(item)['red_1'], dict(item)['red_2'], dict(item)['red_3'], dict(item)['red_4'], dict(item)['red_5'], dict(item)['red_6'], dict(item)['blue_1'], dict(item)['happy_sunday'], dict(item)['prize_pool_bonus'], dict(item)['first_prize_count'], dict(item)['first_prize_bonus'], dict(item)['second_prize_count'], dict(item)['second_prize_bonus'], dict(item)['total_betting_amount'], dict(item)['lottery_date'])
        try:
            self.cursor.execute(sql)
            self.conn.autocommit('on')
        except Exception as e:
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()

# 将item保存为json文件
class LotteryPipelineJson(object):
    def __init__(self):
        self.f = open('shuangseqiu.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        print type(item)
        return item

    def close_spider(self, spider):
        pass




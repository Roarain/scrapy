# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import MySQLdb


# 将items返回到cmd终端
# class SlotteryPipeline(object):
#     def process_item(self, item, spider):
#         return item

# 将item保存到mysql
class SlotteryPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='abcd1234', host='127.0.0.1', port=3306, db='webapp', use_unicode=True, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into daletou_history(lottery_number, front_1, front_2, front_3, front_4, front_5, back_1, back_2, prize_pool_bonus, first_prize_count, first_prize_bonus, second_prize_count, second_prize_bonus, total_betting_amount, lottery_date) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (dict(item)['lottery_number'], dict(item)['front_1'], dict(item)['front_2'], dict(item)['front_3'], dict(item)['front_4'], dict(item)['front_5'], dict(item)['back_1'], dict(item)['back_2'], dict(item)['prize_pool_bonus'], dict(item)['first_prize_count'], dict(item)['first_prize_bonus'], dict(item)['second_prize_count'], dict(item)['second_prize_bonus'], dict(item)['total_betting_amount'], dict(item)['lottery_date'])
        try:
            self.cursor.execute(sql)
            self.conn.autocommit('on')
        except Exception as e:
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()

# 将item保存为json文件
class SlotteryPipelineJson(object):
    def __init__(self):
        self.f = open('daletou.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        print type(item)
        return item

    def close_spider(self, spider):
        pass
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb


# 将item保存到mysql
class CloPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='abcd1234', host='localhost', port=3306, db='webapp', use_unicode=True, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into sales_statistics(hall_name, game_lhdb, game_xywc, game_kxyk, game_shxw, game_sjfg, game_hysj, game_qwgef, daily_turnover, date_time) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (item['hall_name'], dict(item)['game_lhdb'], dict(item)['game_xywc'], dict(item)['game_kxyk'], dict(item)['game_shxw'], dict(item)['game_sjfg'], dict(item)['game_hysj'], dict(item)['game_qwgef'], dict(item)['daily_turnover'], dict(item)['date_time'])
        try:
            self.cursor.execute(sql)
            self.conn.autocommit('on')
        except Exception as e:
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()


# 将item保存为json文件
class CloPipelineJson(object):
    def __init__(self):
        self.f = open('zfzx.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()

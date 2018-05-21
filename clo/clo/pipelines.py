# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import MySQLdb
from mysqlpool import MysqlPool
import pymongo

'''
# 将item保存到mysql
class CloPipeline(object):
    def __init__(self):
        self.mp = MysqlPool()

    def process_item(self, item, spider):
        sql = 'insert into sales_statistics(hall_name, game_lhdb, game_xywc, game_kxyk, game_shxw, game_sjfg, game_hysj, game_qwgef, daily_turnover, date_time) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (item['hall_name'], dict(item)['game_lhdb'], dict(item)['game_xywc'], dict(item)['game_kxyk'], dict(item)['game_shxw'], dict(item)['game_sjfg'], dict(item)['game_hysj'], dict(item)['game_qwgef'], dict(item)['daily_turnover'], dict(item)['date_time'])
        try:
            self.mp.execute_sql(sql)
        except Exception as e:
            self.mp.end('rollback')
        return item

    def close_spider(self, spider):
        self.mp._cursor.close()
'''
'''
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
'''


# 将item保存到mongoDB
class CloPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.client['zfzx']
        self.collection = self.db['sale_statistics']

    def process_item(self, item, spider):
        post_item = dict(item)
        self.collection.insert(post_item)
        return len(item)

    def close_spider(self, spider):
        pass


'''
class CloPipeline(object):
    def __init__(self):
        self.f = open('zfzx.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()
'''
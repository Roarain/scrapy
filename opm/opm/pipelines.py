# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo

'''
class OpmPipelineJson(object):
    def __init__(self):
        self.f = open('opm.json', 'w')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()
'''


class OpmPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.db = self.client['opm']
        self.collection = self.db['terminal_statistics']

    def process_item(self, item, spider):
        post_item = dict(item)
        self.collection.insert(post_item)
        return len(item)

    def close_spider(self, spider):
        self.client.close()


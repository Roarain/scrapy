# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import MySQLdb


# 将item保存到mysql
class MgaPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='abcd1234', host='127.0.0.1', port=3306, db='webapp', use_unicode=True, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into licensed(company_name, reg_no, license_number, license_class, platform, status, registered_address, termination_date, entity_telephone_number, general_email_address) values ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (dict(item)['company_name'], dict(item)['reg_no'], dict(item)['license_number'], dict(item)['license_class'], dict(item)['platform'], dict(item)['status'], dict(item)['registered_address'], dict(item)['termination_date'], dict(item)['entity_telephone_number'], dict(item)['general_email_address'])
        try:
            self.cursor.execute(sql)
            self.conn.autocommit('on')
        except Exception as e:
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.conn.close()

# 将item保存为json文件
class MgaPipelineJson(object):
    def __init__(self):
        self.f = open('licensed.json', 'wb')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.f.write(content)
        print type(item)
        return item

    def close_spider(self, spider):
        pass

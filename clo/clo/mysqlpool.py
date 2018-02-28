# -*- coding: utf-8 -*-

"""
@purpose: 
@version: 1.0
@author: Roarain
@time: 2018/2/27 9:41
@contact: welovewxy@126.com
@file: mysqlconn.py
@license: Apache Licence
@site: 
@software: PyCharm
"""

import MySQLdb
from MySQLdb.cursors import DictCursor
import DBUtils
from DBUtils.PooledDB import PooledDB
import mysqlconf
import logging

logging.basicConfig(filename='mysqlconn.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(level=logging.DEBUG)


class MysqlPool(object):
    __pool = None

    def __init__(self):
        self._conn = MysqlPool.__get_conn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __get_conn():
        if not MysqlPool.__pool:
            __pool = PooledDB(creator=MySQLdb,
                              mincached=1,
                              maxcached=20,
                              host=mysqlconf.DB_HOST,
                              port=mysqlconf.DB_PORT,
                              user=mysqlconf.DB_USER,
                              passwd=mysqlconf.DB_PASSWORD,
                              db=mysqlconf.DB_NAME,
                              use_unicode=False,
                              charset=mysqlconf.DB_CHAR,
                              cursorclass=DictCursor,
                              )
        return __pool.connection()

    def execute_sql(self, sql):
        self._cursor.execute(sql)
        return self._fetch_result()

    def _fetch_result(self):
        result = self._cursor.fetchall()
        return result

    # def insert_one(self, sql, value):
    #     self._cursor.execute(sql, value)
    #     return self._get_insert_id()
    #
    # def insert_many(self, sql, values):
    #     count = self._cursor.execute(sql, values)
    #     return count
    #
    # def _get_insert_id(self):
    #     self._cursor.execute("SELECT @@IDENTITY AS id")
    #     result = self._cursor.fetchall()
    #     return result[0]['id']
    #
    # def __query(self, sql, param=None):
    #     if not param:
    #         count = self._cursor.execute(sql)
    #     elif param:
    #         count = self._cursor.execute(sql, param)
    #     return count

    def begin(self):
        self._conn.autocommit(0)

    def end(self, option='commit'):
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self, isEnd=1):
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()

if __name__ == '__main__':
    mp = MysqlPool()
    # sql_statement = 'select count(*) from t1'
    sql_statement = 'insert into t1 values(4,"dog4")'
    mp.execute_sql(sql_statement)
    # mp.dispose()
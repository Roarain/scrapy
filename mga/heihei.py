# -*- coding: utf-8 -*-

"""
@purpose: 
@version: 1.0
@author: Roarain
@time: 2018/3/8 19:05
@contact: welovewxy@126.com
@file: heihei.py
@license: Apache Licence
@site: 
@software: PyCharm
"""
import MySQLdb
import logging

logging.basicConfig(filename='heihei.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(level=logging.DEBUG)

A = ['a1', 'a2', 'a3']
B = ['b1', 'b2', 'b3']
C = ['c1', 'c2', 'c3']


if len(A) == len(B) == len(C):
    conn = MySQLdb.connect(user='root', passwd='abcd1234', host='127.0.0.1', port=3306, db='webapp',
                           use_unicode=True, charset='utf8')
    cursor = conn.cursor()
    for i in range(len(A)):
        sql = 'insert into heihei(name1, name2, name3) values ("%s", "%s", "%s")' % (A[i], B[i], C[i])
        try:
            cursor.execute(sql)
            conn.autocommit('on')
        except Exception as e:
            conn.rollback()

    conn.close()


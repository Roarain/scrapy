# -*- coding: utf-8 -*-

"""
@purpose: 
@version: 1.0
@author: Roarain
@time: 2018/2/27 9:42
@contact: welovewxy@126.com
@file: mysqlconf.py
@license: Apache Licence
@site: 
@software: PyCharm
"""

import logging

logging.basicConfig(filename='mysqlconf.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(level=logging.DEBUG)

DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = 'abcd1234'
DB_NAME = 'webapp'
DB_CHAR = 'utf8'

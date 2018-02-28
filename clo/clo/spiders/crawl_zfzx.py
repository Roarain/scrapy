# -*- coding: utf-8 -*-

"""
@purpose: 
@version: 1.0
@author: Roarain
@time: 2018/2/26 10:23
@contact: welovewxy@126.com
@file: crawl_zfzx.py
@license: Apache Licence
@site: 
@software: PyCharm
"""

import os
import logging
import datetime
import threading
import subprocess
import multiprocessing
import time

logging.basicConfig(filename='crawl_zfzx.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(level=logging.DEBUG)


def exec_crawl(cmd):
    try:
        logging.info("开始执行 %s" % (cmd))
        os.popen(cmd)
        # subprocess.call(cmd, shell=True)
        logging.info("结束执行 %s" % (cmd))
    except Exception as e:
        logging.info("执行失败 %s" % (cmd))


if __name__ == "__main__":
    logging.info("开始时间 %s" % (datetime.datetime.now()))
    pool = multiprocessing.Pool(processes=50)

    for i in xrange(2000):
        cmd = 'scrapy crawl zfzx -a day_number=%d --nolog' % (i)
        pool.apply_async(exec_crawl, (cmd,))

    '''
    number = 0
    while number < 21:
        start = number * 100
        end = (number + 1) * 100
        for i in xrange(start, end):
            cmd = 'scrapy crawl zfzx -a day_number=%d --nolog' % (i)
            pool.apply_async(exec_crawl, (cmd, ))
        time.sleep(360)
        number += 1
    '''
    pool.close()
    pool.join()
    logging.info("结束时间 %s" % (datetime.datetime.now()))

'''
if __name__ == '__main__':
    thread_list = []

    logging.info("开始时间 %s" % (datetime.datetime.now()))
    for i in range(50):
        cmd = 'scrapy crawl zfzx -a day_number=%d --nolog' % (i)
        th = threading.Thread(target=exec_crawl, args=(cmd, ))
        th.setDaemon(True)
        th.start()
        thread_list.append(th)

    for th in thread_list:
        th.join()

    logging.info("结束时间 %s" % (datetime.datetime.now()))
'''
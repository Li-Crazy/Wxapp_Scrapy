
'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/6/4 20:25
@Software: PyCharm
@File    : start.py
'''
from scrapy import cmdline
cmdline.execute("scrapy crawl wxapp_spider".split())
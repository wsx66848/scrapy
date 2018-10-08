# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import codecs
import time


class WrdSpiderPipeline(object):

    def __init__(self):
        filename = "url-%s.csv" % time.strftime("%Y-%m-%d|%H:%M:%S", time.localtime())
        self.c = open(filename, 'ab')
        self.c.write(codecs.BOM_UTF8)
        self.file = csv.writer(self.c)

    def process_item(self, item, spider):
        self.file.writerow([item.get('title'), item.get('url'), item.get('root_url'), item.get('description'), item.get('host')])
        return item

    def close_spider(self, spider):
        self.c.close()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JianshuSpiderPipeline(object):

    def __init__(self):
        dbparams ={
            'host':'127.0.0.1',
            'user':'root',
            'password':'131415',
            'database':'jianshu',
            'port':3306,
            'charset':'utf8'
        }
        self.db = pymysql.connect(**dbparams)
        self.cursor = self.db.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['author'],item['content'],item['pub_time'],
                            item['origin_url'],item['word_count'],item['read_count'],item['like_count']))
        self.db.commit()


        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql  = '''
            INSERT INTO jianshu_spider(id,title,author,content,pub_time,origin_url,word_count,read_count,like_count)
            VALUES (NULL ,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
        return self._sql
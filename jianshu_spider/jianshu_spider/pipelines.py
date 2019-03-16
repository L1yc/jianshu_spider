# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi

class JianshuSpiderPipeline(object):

    def __init__(self):
        self.dbparams ={
            'host':'127.0.0.1',
            'user':'root',
            'password':'131415',
            'port':3306,
            'database':'jianshu',
            #在存储过程中出现四字节不兼容错误，故将编码改为utf8mb4
            'charset':'utf8mb4',
            #指定cursor的类
            'cursorclass':cursors.DictCursor
        }
        #创建连接池
        self.dbpoor = adbapi.ConnectionPool('pymysql',**self.dbparams)
        self._sql = None

    def process_item(self, item, spider):
        defer = self.dbpoor.runInteraction(self.insert_item,item)
        #增加异常处理
        defer.addErrback(self.handle_error,item)


    def insert_item(self,cursor,item):
        cursor.execute(self.sql,(item['title'],item['author'],item['content'],item['pub_time'],
                            item['origin_url'],item['word_count'],item['read_count'],item['like_count']))

    def handle_error(self,error,item):
        print("="*60)
        print(error)
        print("="*60)

    @property
    def sql(self):
        if not self._sql:
            self._sql  = '''
            INSERT INTO js(id,title,author,content,pub_time,origin_url,word_count,read_count,like_count)
            VALUES (NULL ,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
        return self._sql
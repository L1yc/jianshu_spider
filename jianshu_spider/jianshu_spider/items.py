# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    '''爬取内容
        title ： 文章标题
        author ： 作者
        content ： 发布时间
        origin_url : 文章链接
        word_count : 字数
        read_count : 阅读次数
        like_count : 喜欢数

    '''

    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    origin_url = scrapy.Field()
    pub_time = scrapy.Field()
    read_count = scrapy.Field()
    word_count = scrapy.Field()
    like_count = scrapy.Field()
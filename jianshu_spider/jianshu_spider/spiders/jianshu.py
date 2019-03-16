# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.response.html import HtmlResponse
from jianshu_spider.items import JianshuItem
import re

class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'./p/*[1-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        content = response.xpath("//div[@class='show-content']").get()
        origin_url = response.url
        pub_time = response.xpath("//span[@class='publish-time']/text()").get().replace('*','')
        word_count = response.xpath("//span[@class='wordage']/text()").get()
        word_count = re.sub(r'\D*','',word_count)

        #read_count&like_count 无法直接拿到，为ajax加载后的数据
        read_count = response.xpath("//span[@class='views-count']/text()").get()
        if read_count:
            read_count = re.sub(r'\D*','',read_count)
        like_count = response.xpath("//span[@class='likes-count']/text()").get()
        if like_count:
            like_count = re.sub(r'\D*','',like_count)
        item = JianshuItem(title=title,author=author,content=content,origin_url=origin_url,
                           pub_time=pub_time,word_count=word_count,read_count=read_count,like_count=like_count)

        yield item

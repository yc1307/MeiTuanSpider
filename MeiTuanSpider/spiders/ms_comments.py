# -*- coding: utf-8 -*-
import json
import re
import time

import scrapy

from MeiTuanSpider.items import MeituanBranditem, MeituanCommentItem


class MsCommentsSpider(scrapy.Spider):
    name = 'ms_comments'
    allowed_domains = ['meituan.com']
    start_urls = ['http://hf.meituan.com/meishi/pn1/']
    brand_url = 'http://hf.meituan.com/meishi/pn{}/'
    comment_url = [
        'http://www.meituan.com/meishi/api/poi/getMerchantComment?platform=1&partner=126&id={0}&offset={1}&pageSize=10']

    def start_requests(self):
        for i in range(1, 33):
            yield scrapy.Request(
                url=self.brand_url.format(i),
                # 转至parse函数中,对单个页面处理
                callback=self.parse
            )
        time.time(1000)
    def parse(self, response):
        brand_list = re.findall(r'"poiLists":(.*?),"comHeader"', response.body.decode())[0]
        brand_list = json.loads(brand_list)
        item_list = []
        for li in brand_list['poiInfos']:
            item = MeituanBranditem()
            item['BrandId'] = li['poiId']
            item['Brand'] = li['title']
            item['Addr'] = li['address']
            item['CommentNum'] = li['allCommentNum']
            item_list.append(item)
            # print(item)
            CommentNum = int(item['CommentNum']) // 10
            for i in range(CommentNum):
                yield scrapy.Request(
                    url=self.comment_url[0].format(item['BrandId'], i * 10),
                    callback=self.parse_comments,
                    meta={'item': item}
                )
            yield item

    def parse_comments(self, response):
        item = response.meta['item']
        html = json.loads(response.body.decode())
        c_list = html['data']['comments']
        for c in c_list:
            c_item = MeituanCommentItem()
            c_item['Brand'] = item['Brand']
            c_item['BrandId'] = item['BrandId']
            c_item['userName'] = c['userName']
            c_item['userId'] = c['userId']
            c_item['comment'] = c['comment']
            c_item['star'] = int(c['star']) / 10
            print(c_item)
            yield c_item

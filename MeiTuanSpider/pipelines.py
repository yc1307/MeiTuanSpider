# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from MeiTuanSpider.items import MeituanBranditem, MeituanCommentItem


class MeituanspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    # 数据库登录需要帐号密码时使用，无则跳过
    # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])

    def open_spider(self, spider):
        client = pymongo.MongoClient(
            host=settings['MONGODB_HOST'],
            port=settings['MONGODB_PORT']
        )
        self.db = client[settings['MONGODB_DBNAME']]
        self.collection = self.db[settings['MONGODB_COL_BRAND']]
        # 由于不能同时开启多个,使用isinstance进行判断

    def process_item(self, item, spider):

        # """不同的item类型，放入不同的集合中"""
        if isinstance(item, MeituanBranditem):
            brand_infos = dict(item)
            self.collection.insert(brand_infos)

        if isinstance(item, MeituanCommentItem):
            comments_infos = dict(item)
            self.collection = self.db[settings['MONGODB_COL_COMMENT']]
            self.collection.insert(comments_infos)

        return item

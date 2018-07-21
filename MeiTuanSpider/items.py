# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MeituanBranditem(scrapy.Item):
    BrandId = scrapy.Field()
    Brand = scrapy.Field()
    Addr = scrapy.Field()
    CommentNum = scrapy.Field()


class MeituanCommentItem(scrapy.Item):
    BrandId = scrapy.Field()
    Brand = scrapy.Field()
    userName = scrapy.Field()
    userId = scrapy.Field()
    comment = scrapy.Field()
    star = scrapy.Field()

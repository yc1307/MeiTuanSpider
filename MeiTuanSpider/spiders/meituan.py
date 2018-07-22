# -*- coding: utf-8 -*-
import json

import scrapy
import demjson
import time


class MeituanSpider(scrapy.Spider):
    name = 'meituan'
    allowed_domains = ['www.meituan.com']
    start_urls = ['https://hf.meituan.com/']
    # CityId_list = [1, 10, 20, 30, 40, 42, 44, 45, 50, 51]
    CityId_list = [56,]
    api_url = [
        'http://api.meituan.com/group/v4/deal/select/city/{cityid}/cate/1?sort=solds&hasGroup=true&mpt_cate1=1&offset={os}&limit=100']
    # self.api_url = 'http://api.meituan.com/group/v4/deal/select/city/1/cate/1?sort=solds&hasGroup=true&mpt_cate1=1&offset=0&limit=100'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Host': 'api.meituan.com',
        'Connection': 'Keep-Alive'
    }

    def start_requests(self):

        for cityid in self.CityId_list:
            for i in range(3000):
                yield scrapy.Request(
                    url=self.api_url[0].format(cityid=cityid, os=str(i * 100)),
                    # 转至parse函数中,对单个页面处理
                    callback=self.parse
                )
            time.sleep(10)

    def parse(self, response):
        print('--------------')
        itemlist = []
        info_dict = json.loads(response.text)
        info_list = info_dict['data']
        for info in info_list:
            item = {}
            # 店铺名称
            item['name'] = info['poi']['name']
            # 所在区
            if info['poi']['addr'][2] == '区':
                item['distName'] = info['poi']['addr'][0:2]
            else:
                item['distName'] = ''
            # 所属片区
                item['areaName'] = info['poi']['areaName']
            # 详细地址
            item['addr'] = info['poi']['addr']
            # 纬度
            item['lat'] = info['poi']['lat']
            # 经度
            item['lng'] = info['poi']['lng']
            # 餐厅类别
            item['cateName'] = info['poi']['cateName']
            # 优惠套餐情况
            abstracts = ''
            for abstract in info['poi']['payAbstracts']:
                # abstracts.append(abstract['abstract'])
                item['abstracts'] = abstracts + abstract['abstract'] + ';'
            # 评分
            item['avgScore'] = info['poi']['avgScore']
            # 营业时间
            item['openInfo'] = info['poi']['openInfo'].replace('\n', ' ')
            # 联系电话
            item['phone'] = info['poi']['phone']
            # 累计售出份数
            item['historyCouponCount'] = info['poi']['historyCouponCount']
            # 餐厅简介
            item['introduction'] = info['poi']['introduction']
            # 特色菜
            item['featureMenus'] = info['poi']['featureMenus']
            print(item)
            print('--------------------------')
            itemlist.append(item)
            yield item

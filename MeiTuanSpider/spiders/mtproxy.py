# -*- coding: utf-8 -*-
import scrapy


class MtproxySpider(scrapy.Spider):
    name = 'mtproxy'
    # allowed_domains = ['list.jd.com']
    # start_urls = ['https://list.jd.com/list.html?cat=9987,653,655']
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']
    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': {
    #         # 写你spider 的中间件的路径
    #         'MeiTuanSpider.middlewares.ProxyMiddleware': 2,
    #     },
    #     # 下载超时 5- 10 秒
    #     'DOWNLOAD_TIMEOUT': 10,
    #     # 下载重试次数 2 -3 次
    #     'RETRY_TIMES': 3,
    # }

    # def parse(self, response):
    #     li_list = response.xpath('//ul[@class="gl-warp clearfix"]/li')
    #     for li in li_list:
    #         item = {}
    #
    #         item['sj_url'] = 'https:' + li.xpath('./div/div/a/@href').extract_first()
    #         print(item['sj_url'])
    #         yield scrapy.Request(
    #             url=item['sj_url'],
    #             meta={'item':item},
    #             callback=self.parse_detail
    #         )
    #
    # def parse_detail(self, response):
    #     item = response.meta['item']
    #     print(response.text)

    def parse(self, response):
        # 匹配出ip
        print(response.text)
        data = response.xpath('//span[@class="c-gap-right"]/text()').extract()
        print(data)

# -*- coding: utf-8 -*-

# Scrapy settings for MeiTuanSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MeiTuanSpider'

SPIDER_MODULES = ['MeiTuanSpider.spiders']
NEWSPIDER_MODULE = 'MeiTuanSpider.spiders'

LOG_LEVEL = 'WARNING'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3495.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   # 'MeiTuanSpider.middlewares.IPPoolsMiddleware': 543,
   'MeiTuanSpider.middlewares.RandomUserAgentMiddleware': 125,
   # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 123,
   # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 125,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'MeiTuanSpider.middlewares.MeituanspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #    'MeiTuanSpider.pipelines.MeituanspiderPipeline': 300,
    'MeiTuanSpider.pipelines.MongoDBPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'MeiTuan'

MONGODB_COL_BRAND = 'BrandInfo'
MONGODB_COL_COMMENT = 'CommentInfo'

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1',
    'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'
]

IPPOOLS = [
    {'ip': '47.90.87.225:88'},
    {'ip': '103.61.100.97:8080'},
    {'ip': '202.63.243.167:53281'},
    {'ip': '78.111.120.233:53281'},
    {'ip': '202.93.228.34:53281'},
    {'ip': '101.110.118.24:8088'},
    {'ip': '14.102.50.11:8080'},
    {'ip': '197.210.165.66:53281'},
    {'ip': '212.19.96.71:41258'},
    {'ip': '117.44.247.49:8908'},
    {'ip': '103.55.69.242:53281'},
    {'ip': '117.44.247.53:8908'},
    {'ip': '172.254.60.170:8080'},
    {'ip': '101.110.119.66:93'},
    {'ip': '58.247.46.123:8088'},
    {'ip': '185.93.204.132:41258'},
    {'ip': '46.175.253.242:41258'},
    {'ip': '115.213.240.68:9000'},
    {'ip': '185.18.141.40:41258'},
    {'ip': '95.143.111.2:41258'},
    {'ip': '150.242.109.124:53281'},
    {'ip': '31.179.192.216:8080'},
    {'ip': '42.112.15.116:53281'},
    {'ip': '103.225.69.3:53281'},
    {'ip': '101.96.11.37:8090'},
    {'ip': '188.239.118.227:41258'},
    {'ip': '101.110.118.60:80'},
    {'ip': '101.110.118.20:8090'},
    {'ip': '101.96.10.72:80'},
    {'ip': '91.211.107.204:41258'},
    {'ip': '81.211.100.158:8080'},
    {'ip': '85.91.119.6:8080'},
    {'ip': '38.103.239.13:35617'},
    {'ip': '95.78.173.238:53281'},
    {'ip': '103.16.165.99:53281'},
    {'ip': '186.83.66.5:63909'},
    {'ip': '81.15.203.30:41258'},
    {'ip': '31.173.222.141:8080'},
    {'ip': '80.94.30.234:8080'},
    {'ip': '39.104.77.237:8080'},
    {'ip': '178.54.6.178:53281'},
    {'ip': '200.146.226.75:8080'},
    {'ip': '101.96.11.40:87'},
    {'ip': '190.90.193.27:53281'},
    {'ip': '196.22.55.22:53281'},
    {'ip': '87.244.181.115:8080'},
    {'ip': '103.94.122.254:8080'},
    {'ip': '36.66.226.185:8080'},
    {'ip': '200.114.102.129:53281'},
    {'ip': '114.141.57.50:53281'},
    {'ip': '41.169.154.2:8080'},
    {'ip': '80.150.65.6:8080'},
    {'ip': '91.234.183.25:53281'},
    {'ip': '101.96.11.39:83'},
    {'ip': '101.96.11.37:8089'},
    {'ip': '123.57.61.38:8118'},
    {'ip': '31.25.129.84:8080'},
    {'ip': '90.151.59.120:8080'},
    {'ip': '117.90.4.187:9000'},
    {'ip': '178.33.178.217:80'},
    {'ip': '37.221.249.37:8080'},
    {'ip': '92.247.95.173:53281'},
    {'ip': '103.16.165.226:53281'},
    {'ip': '101.110.119.63:80'},
    {'ip': '189.58.101.69:53281'},
    {'ip': '169.255.5.174:53281'},
    {'ip': '103.94.112.90:8080'},
    {'ip': '31.25.137.182:8080'},
    {'ip': '91.200.44.190:8080'},
    {'ip': '222.175.200.58:8060'},
    {'ip': '181.211.166.105:54314'},
    {'ip': '77.75.6.34:8080'},
    {'ip': '217.12.212.150:24'},
    {'ip': '138.121.33.6:53281'},
    {'ip': '37.187.178.194:808'},
    {'ip': '69.63.67.43:8080'},
    {'ip': '91.92.10.112:8080'},
    {'ip': '95.105.254.219:8080'},
    {'ip': '213.222.34.200:53281'},
    {'ip': '92.38.47.226:80'},
    {'ip': '103.85.64.212:53281'},
    {'ip': '101.96.10.36:8088'},
    {'ip': '39.104.13.181:8080'},
    {'ip': '83.215.247.182:53281'},
    {'ip': '121.121.125.55:80'},
    {'ip': '77.85.169.28:8080'},
    {'ip': '39.104.62.1:8080'},
    {'ip': '103.88.234.90:53281'},
    {'ip': '39.137.69.10:80'},
    {'ip': '182.93.91.244:80'},
    {'ip': '101.96.11.36:86'},
    {'ip': '103.79.11.23:53281'},
    {'ip': '91.185.47.156:8080'},
    {'ip': '168.253.73.227:53281'},
    {'ip': '222.222.236.207:8060'},
]

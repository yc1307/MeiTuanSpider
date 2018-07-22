# -*- coding: utf-8 -*-
import os
import sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# execute(['scrapy', 'crawl', 'meituan'])
# execute(['scrapy', 'crawl', 'ms_comments'])
execute(['scrapy', 'crawl', 'mtproxy'])
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 11:40
# @Author  : XiZhi
# @File    : proxies_test.py
import requests

# local_url = 'localhost:5555'
local_url = 'http://127.0.0.1:5555/random'


def get_proxy():
    try:
        response = requests.get(url=local_url)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


def crawl():
    proxy = get_proxy()
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }

    res = requests.get(url='http://meituan.com', proxies=proxies)
    print(res.status_code)
    if res.status_code == 200:
        print(res.text)


if __name__ == '__main__':
    crawl()

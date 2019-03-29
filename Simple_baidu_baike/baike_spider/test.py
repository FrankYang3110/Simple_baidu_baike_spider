#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# a = set()
# print(a is None)

# def get():
#     return
# a = get()
# print(a is None)
from fake_useragent import UserAgent
import re
import requests
from urllib.parse import urljoin
from lxml import etree

headers = {'User-Agent': UserAgent().random}
url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'

r = requests.get(url, headers=headers)
r.encoding = r.apparent_encoding
base_url = r.url
html  = r.text
tree = etree.HTML(html)
hrefs = tree.xpath('//a[contains(@href,"/item")]/@href')

# pattern  = re.compile(r'href="(/item.*?)"')
# urls = re.findall(pattern, html)
# for url in urls:
#     new_url = urljoin(base_url, url)
#     print(new_url)

# href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80/7073760"
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from lxml import etree
import re
from urllib.parse import urljoin


class Parser(object):
    def parse(self, page_url, html):
        if page_url is None or html is None:
            return
        new_urls = self.get_new_urls_by_re(page_url, html)
        new_data = self.get_new_data(page_url, html)
        return new_urls, new_data

    # 方式一：用正则匹配百科网址
    def get_new_urls_by_re(self, page_url, html):
        url_set = set()
        pattern = re.compile(r'href="(/item.*?)"')
        hrefs = re.findall(pattern, html)
        for href in hrefs:
            new_url = urljoin(page_url,href)
            url_set.add(new_url)
        return url_set

    # 方式二：用xpath获取链接
    def get_new_urls_by_xpath(self, page_url, html):
        url_set = set()
        tree = etree.HTML(html)
        hrefs = tree.xpath('//a[contains(@href,"/item")]/@href')
        for href in hrefs:
            new_url = urljoin(page_url, href)
            url_set.add(new_url)

    def get_new_data(self, page_url, html):
        tree = etree.HTML(html)
        data = {}
        data['url'] = page_url
        data['title'] = tree.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()')[0]
        summary_list = tree.xpath('//div[@class="lemma-summary"]/div[1]//text()')
        data['summary'] = ''.join(summary_list)
        return data







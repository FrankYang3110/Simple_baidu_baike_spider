#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from url_manager import UrlManager
from downloader import Downloader
from _parser import Parser
from data_output import DadaOutput


class Scheduler(object):
    def __init__(self):
        self.url_manager = UrlManager()
        self.downloader = Downloader()
        self.parser = Parser()
        self.data_output = DadaOutput()

    def crawl(self, start_url, max_page):
        self.url_manager.add_new_url(start_url)
        while self.url_manager.has_url() and self.url_manager.old_url_size() < max_page:
            page_url = self.url_manager.get_new_url()
            page_html = self.downloader.down(page_url)
            new_urls, new_data = self.parser.parse(start_url, page_html)
            self.url_manager.add_new_urls(new_urls)
            self.data_output.store_data(new_data)
            self.data_output.output_html()
            print('第%s条数据写入' % (self.url_manager.old_url_size()))


if __name__ == '__main__':
    max_page = 100
    scheduler = Scheduler()
    scheduler.crawl('https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA', max_page)










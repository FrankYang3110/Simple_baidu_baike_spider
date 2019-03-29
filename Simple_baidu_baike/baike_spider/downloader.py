#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from fake_useragent import UserAgent


class Downloader(object):
    def __init__(self):
        self.headers = {'User-Agent': UserAgent().random}

    def down(self, url):
        if url is None:
            return None
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        else:
            print('get html failed, the url is: %s' % url)

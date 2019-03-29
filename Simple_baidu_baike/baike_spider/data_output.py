#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import codecs


class DadaOutput(object):
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open("baike.html", "a", encoding="utf-8") as file:
            file.write("<html>")
            # 下添加的head标签和meta标签告诉浏览器此html文件的编码方式，不然会产生乱码。
            file.write("<head>")
            file.write("<meta ")
            file.write('http-equiv="Content-Type" content="text/html; charset=utf-8" /')
            file.write(">")
            file.write("</head>")
            file.write("<body>")
            file.write("<table>")
            for data in self.datas:
                file.write('<tr>')
                file.write('<td>%s</td>' % data['url'])
                file.write('<td>%s</td>' % data['title'])
                file.write('<td>%s</td>' % data['summary'])
                file.write('</tr>')
                self.datas.remove(data)
            file.write("</table>")
            file.write("</body>")
            file.write("</html>")






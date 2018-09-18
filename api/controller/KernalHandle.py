# -*- coding: utf-8 -*-
# @Time  : 2018/9/18 下午12:01
# @Author: Zhangjingpeng
# @Site  : KernalHandle.py

import tornado.web

class KernalHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
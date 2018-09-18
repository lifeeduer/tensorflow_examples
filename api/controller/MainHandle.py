# -*- coding: utf-8 -*-
# @Time  : 2018/9/17 下午8:48
# @Author: Zhangjingpeng
# @Site  : MainHandle.py

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()


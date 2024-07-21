#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
__@author__ : secoder
__@cnblog__: https://www.cnblogs.com/secoder
__file__   : wsgi
__time__   : 2024/7/14 19:15
__describe__：werkzeug 模拟 wsgi
"""
from werkzeug.serving import run_simple

def test_func():
    print("hi～ 我运行了")
    
class FlaskA(object):
    def __call__(self, *args, **kwargs):
        return "test"

    def run(self):
        run_simple("127.0.0.1", 1234, self)  

    
app = FlaskA()

    
if __name__ == '__main__':
    app.run()

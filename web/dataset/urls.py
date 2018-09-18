# -*- coding: utf-8 -*-
# @Time  : 2018/9/18 下午3:18
# @Author: Zhangjingpeng
# @Site  : urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
]

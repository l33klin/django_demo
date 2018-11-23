#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 20/11/2018 12:54 AM
@Author  : Jian
@Contact : jian.li@shopee.com
@Site    : 
@File    : urls.py
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]

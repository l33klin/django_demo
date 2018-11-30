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

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

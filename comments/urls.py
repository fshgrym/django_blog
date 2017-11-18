#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
from django.conf.urls import url
from . import views
app_name='comments'
urlpatterns=[
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$',views.post_comment,name='post_comment'),
    url(r'^contact/',views.Contact,name='contact')
]
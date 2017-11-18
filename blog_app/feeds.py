#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title='ド゛゜范'
    link='/'#通过聚合阅读器跳转到网站的地址
    description='ド゛゜范的博客'#显示在聚合阅读器上面的描述信息
    #需要显示的内容
    def items(self):
        return Post.objects.all()
    #聚合器中显示的内容
    def item_title(self, item):
        return '[%s] %s' % (item.category,item.title)
    def item_description(self, item):
        return item.body
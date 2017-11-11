#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count

register=template.Library()#注意 Django 1.9 后才支持 simple_tag 模板标签，如果你使用的 Django 版本小于 1.9，你将得到一个错误。Django 1.9 以前的版本如何自定义模板标签这里不再赘述
@register.simple_tag
def get_recent_posts(num=5):#最新文章模板标签
    return Post.objects.all().order_by('-create_time')[:num]
@register.simple_tag
def archives():#归档模板标签
    return Post.objects.dates('create_time','month',order='DESC')#dates返回一个列表 month是精确到第几个月，desc是排序，表明降序，从而帮助我们归档文章
@register.simple_tag
def get_categories():#f分类标签模板
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
@register.simple_tag
def get_tags():
    return Tag.objects.all()
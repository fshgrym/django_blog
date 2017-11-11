#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
from django.conf.urls import url,include
from . import views
from django.conf import settings
from DjangoUeditor import urls as DjangoUeditor_urls
app_name='blog_app'#声明这个url是属于blog_app的
urlpatterns=[
    # url(r'^$',views.index,name='index'),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^$',views.IndexView.as_view(),name='index'),
    # url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)$',views.PostDatailView.as_view(),name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{0,2})/$',views.ArtucleView.as_view(),name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<tag>\w+)/$',views.TagsView.as_view(),name='tag')
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author:fsh
from django import forms
from .models import Comment
# class CommentForm(forms.ModelForm):
#
#     class Meta:
#         model=Comment
#         fields=['name','email','url','text']


class CommentForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"请输入您的名字",'max_length':25}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'请输入您的邮箱'}))
    url=forms.URLField(widget=forms.URLInput(attrs={'class':'form-control','placeholder':'网址'}))
    text=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'评论内容'}))
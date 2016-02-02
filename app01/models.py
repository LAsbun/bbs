#!/usr/bin/env python
# coding:utf-8
from django.db import models

# Create your models here.

#用户类型
class UserType(models.Model):
    display = models.CharField(max_length=50)

    def __unicode__(self):
        return self.display

# 用户
class Admin(models.Model):
    username = models.CharField(max_length=50)

    password = models.CharField(max_length=256)

    email = models.EmailField()

    usertype = models.ForeignKey('UserType')

    def __unicode__(self):
        return self.username
# 新闻类型
class NewsType(models.Model):

    display = models.CharField(max_length=50)

    def __unicode__(self):
        return self.display
#新闻

class News(models.Model):

    title = models.CharField(max_length=50)

    summary = models.CharField(max_length=256)

    url = models.URLField()

    favor_count = models.IntegerField(default=0)

    reply_count = models.IntegerField(default=0)

    newstype = models.ForeignKey('NewsType')

    user = models.ForeignKey('Admin')

    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

#评论
class Reply(models.Model):

    content = models.TextField()

    user = models.ForeignKey('Admin')

    new = models.ForeignKey('News')

    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content

#聊天室
class Chat(models.Model):

    content = models.TextField()

    user = models.ForeignKey('Admin')

    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content
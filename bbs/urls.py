"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from webqq import urls as web11_urls

from app01 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chat/', include(web11_urls)),
    url(r'^index/', views.index, name='index'),
    url(r'^addfavor/', views.addfavor, name='addfavor'),
    url(r'^getreply/', views.getreply, name='getreply'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/',views.logout, name='logout'),
    url(r'^submitreply/', views.submitreply, name='submitreply'),
    url(r'^webchat/', views.webchat, name='webchat'),
    url(r'^freshwebchat/', views.freshwebchat, name='freshwebchat'),
]

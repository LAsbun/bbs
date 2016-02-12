from django.conf.urls import url

from webqq import views

urlpatterns = [
    url('^$', views.deskboard, name='chat'),
    url('^send_msg/$', views.send_msg, name='send_msg'),
]

#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render_to_response, HttpResponse
from app01.models import Admin
from app01.common import try_int, check_login
import json
# Create your views here.

@check_login
def deskboard(request):
    id = request.session.get('is_login')
    #print id
    friends_list = Admin.objects.filter(id=id).values('friends__username', 'friends__id', 'username', 'id')
    #print friends_list
    context = {
        'friends_list': friends_list,
        'username': friends_list[0]['username'],
        'user__id':friends_list[0]['id'],
    }
    return render_to_response('webqq/deskboard.html', context)

@check_login
def send_msg(request):

    '''
    csrfmiddlewaretoken: $.cookie('csrftoken'),
                    from_id: {{ user__id }},
                    to_id:temp.attr('contact-id'),
                    contact_type:temp.attr('contact-type'),
                    msg:msg_txt,

    '''

    msg = request.POST.get('msg')
    from_id = request.POST.get('from_id')
    to_id = request.POST.get('to_id')
    contact_type = request.POST.get('contact_type')

    #print msg,from_id, to_id, contact_type

    return HttpResponse('sddasa')
#!/usr/bin/env python
#coding:utf8
from django.shortcuts import render_to_response, HttpResponse, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt #临时去除csrf
from django.core.serializers.json import DjangoJSONEncoder #django自带序列化
from app01.models import News, Reply, Admin, Chat
import json
import datetime
from datetime import date
from app01.common import try_int


# Create your views here.

#序列化datetime类型
class CJsonEncode(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj,date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,obj)

#检查是否登陆 如没有则进到login界面
def check_login(func):
    def wrap(request):
        if request.session.get('is_login'):
            return func(request)
        else:
            return redirect('/login/',context_instance=RequestContext(request))
    return wrap


#初始化
@check_login
def index(request):
    news_list = News.objects.all()
    context = {
        'news_list':news_list,'login_url':'/logout/', 'login_text':'退出'
    }
    return render_to_response('index.html', context, context_instance=RequestContext(request))

#添加赞
@csrf_exempt
def addfavor(request):

    ret = {'status':0, 'data':'', 'message':'',}
    try:
        id = request.POST.get('nid', None)
        obj = News.objects.get(id=id)
        temp = obj.favor_count + 1
        obj.favor_count = temp
        obj.save()
        ret['data'] = temp
        ret['status'] = 1

    except Exception, e:
        ret['message'] = e.message

    return HttpResponse(json.dumps(ret))


#登陆
def login(request):

    if request.method == 'POST':
        user = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        print user,pwd
        obj = Admin.objects.get(username=user, password=pwd)
        if obj:
            request.session['is_login'] = obj.id

            return redirect('/index/')
        else:
            context = {'login_url':'/login/', 'login_text':'登陆','msg':'用户名或密码错误',}
            return render_to_response('login.html', context,context_instance=RequestContext(request))
    context = {'login_url':'/login/', 'login_text':'登陆',}

    return render_to_response('login.html', context, context_instance=RequestContext(request))
#登出
def logout(request):
    print request.session.get('is_login')
    del request.session['is_login']
    return  redirect('/login/')


#得到全部评论
@csrf_exempt
@check_login
def getreply(request):
    try:
        nid = request.POST.get('nid', None)
        obj = Reply.objects.filter(new__id=nid).values('content', 'user__username','create_date', 'id')
        #print obj[0].user
        reply_list = json.dumps(list(obj),cls=CJsonEncode)
        #print reply_list
        return HttpResponse(reply_list)
    except Exception, e:
        print e.message
        return HttpResponse('404')


#添加评论
@csrf_exempt
@check_login
def submitreply(request):
    ret = {'status':0, 'data':'', 'msg':''}

    try:
        #print 'sasa'
        data = request.POST.get('data')
        nid = request.POST.get('nid')
        id = request.session.get('is_login')

        newsobj = News.objects.get(id=nid)
        #print 'sasa'
        obj = Reply.objects.create(
            content = data,
            user = Admin.objects.get(id=id),
            new = newsobj,
        )
        ret['status'] = 1
        ret['data'] = {'content':obj.content,'user__username':obj.user.username, 'create_date':obj.create_date.strftime('%Y-%m-%d %H:%M:%S')}
        newsobj.reply_count = newsobj.reply_count+1
        newsobj.save()
        return HttpResponse(json.dumps(ret))
    except Exception, e:
        ret['msg'] = '服务器异常'
        #print e.message
        return HttpResponse(json.dumps(ret))

@csrf_exempt
@check_login
def webchat(request):

    ret = {'status':0, 'data':'', 'msg':''}

    try:
        data = request.POST.get('content')
        id = request.session.get('is_login')

        obj = Chat.objects.create(
            content=data,
            user=Admin.objects.get(id=id)
        )

        ret['status'] = 1
        ret['data'] = {'user__username':obj.user.username, 'create_date':obj.create_date.strftime('%Y-%m-%d %H:%M:%S')}
        return HttpResponse(json.dumps(ret))

    except Exception, e:
        ret['msg'] = '服务器异常'
        return HttpResponse(json.dumps(ret))

@csrf_exempt
@check_login
def freshwebchat(request):
    ret = {'last_num':'','data':''}
    try:
        last_num = try_int(request.POST.get('last_num'))

        if last_num == 0:
            data = list(Chat.objects.all()[-10:-1])
        else:
            data = list(Chat.objects.all()[last_num:])

        ret['last_num'] = data[-1]['id']
        ret['data'] = data
        print ret
        return HttpResponse(json.dumps(ret, CJsonEncode))

    except Exception, e:
        return HttpResponse()
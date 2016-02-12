#coding:utf8
#!/usr/bin/env python
__author__ = 'sws'


'''
num：要转换的字符串

'''
def try_int(num, default = 0):
    try:
        return int(num)
    except:
        return default

#检查是否登陆 如没有则进到login界面
def check_login(func):
    def wrap(request):
        if request.session.get('is_login'):
            return func(request)
        else:
            return redirect('/login/',context_instance=RequestContext(request))
    return wrap
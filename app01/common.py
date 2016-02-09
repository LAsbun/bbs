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
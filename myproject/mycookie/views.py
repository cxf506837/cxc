from django.shortcuts import render

#设置cookie
from django.http import HttpResponse
def set_cookie(request):
    response=HttpResponse("<h1>hello world</h1>")
    response.set_cookie('name','zhangsan')#设置cookie
    return response

#获取cookie
from django.http import HttpResponse
def get_cookie(request):
    print(request.COOKIES)#获取cookie
    print(request.COOKIES.get('name'))
    print(request.COOKIES.get('age'))
    return HttpResponse("<h1>hello world</h1>")

#删除cookie
from django.http import HttpResponse
def del_cookie(request):
    response=HttpResponse("<h1>hello world</h1>")
    response.set_cookie('name','zhangsan',max_age=0)
    return response

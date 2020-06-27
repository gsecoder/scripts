from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
import sys,os
import random
from djangopy import settings
from django_redis import get_redis_connection
from web.forms.account import RegisterModelForm
from web.forms.account import SendSmsForm
from django.http import JsonResponse

"""
模块功能：账号相关的功能
    注册
    登陆
"""

def index(request):
    return HttpResponse("sms")

def conn_redis():
    conn = get_redis_connection("default")
    conn.set("username", "userA", ex=10)
    value = conn.get("username")
    print("value: ", value)
    return HttpResponse("ok")

def register(request):
    """ 用户注册 """
    form = RegisterModelForm()
    return render(request, 'web/account.html', {"form": form})

def send_sms(request):
    """
        发送短信
        根据不同的功能获取不同的短信模板进行短信的发送
            注册验证码：646235
            登陆验证码：646236
    """
    form = SendSmsForm(request, data=request.GET)
    if form.is_valid():
        return JsonResponse({
            "status": True
        })
    return JsonResponse({"status": False, "error": form.errors})



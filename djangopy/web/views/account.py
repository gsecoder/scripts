from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
import sys,os
from util.tencent_sms import send_sms_single
import random
from djangopy import settings
from django_redis import get_redis_connection
from web.forms.account import RegisterModelForm

"""
模块功能：账号相关的功能
    注册
    登陆
"""

sys.path.append(os.path.dirname(__file__) + os.sep )

def index(request):
    return HttpResponse("sms")

def conn_redis():
    conn = get_redis_connection("default")
    conn.set("username", "userA", ex=10)
    value = conn.get("username")
    print("value: ", value)
    return HttpResponse("ok")

def send_sms(request):
    """
        发送短信
        根据不同的功能获取不同的短信模板进行短信的发送
            注册验证码：646235
            登陆验证码：646236
    """
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse("模板不存在")
    code = random.randrange(100000, 1000000)
    res = send_sms_single("17729291319", template_id, [code,])
    print(res)
    if res['result'] == 0:
        return HttpResponse("成功")
    else:
        return HttpResponse(res["errmsg"])

def register(request):
    form = RegisterModelForm()
    return render(request, 'web/account.html', {"form": form})

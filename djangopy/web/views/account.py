from django.shortcuts import HttpResponse

# Create your views here.
import sys,os
from util.tencent_sms import send_sms_single
import random
from djangopy import settings
from django_redis import get_redis_connection

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


from django import forms
from web import models
from django.shortcuts import render
from django.core.validators import RegexValidator
from django.core.validators import ValidationError

class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label="手机号", widget=forms.PasswordInput(), validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    password = forms.CharField(label="密码", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="重复密码", widget=forms.PasswordInput())
    code = forms.CharField(label="验证码", widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        fields = ["username", "email", "mobile_phone", "code", "password", "confirm_password"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = "请输入%s" % (field.label, )

def register(request):
    form = RegisterModelForm()
    return render(request, 'web/register.html', {"form": form})

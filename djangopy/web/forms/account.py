#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : account.py
__time__    : 2020/6/27 16:16
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

from django import forms
from web import models
from django.shortcuts import render
from django.core.validators import RegexValidator
from django.core.validators import ValidationError
from django.conf import settings
import random
from util.tencent.tencent_sms import send_sms_single
from django_redis import get_redis_connection

class RegisterModelForm(forms.ModelForm):
    mobile_phone = forms.CharField(label="手机号", validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
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

class SendSmsForm(forms.Form):
    # 想把对短信模板校验的方法放在钩子函数中进行统一的判断，借用父类的__init__方法
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    mobile_phone = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误')]
    )

    def clean_mobile_phone(self):
        """ 手机号校验的钩子函数"""
        mobile_phone = self.cleaned_data["mobile_phone"]

        """ 判断短信验证码模板 """
        tpl = self.request.GET.get("tpl")
        template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
        if not template_id:
            raise ValidationError("短信模板不存在")

        """ 校验数据库中是否已存在手机号 """
        exists = models.UserInfo.objects.filter(mobile_phone=mobile_phone)
        if exists:
            raise ValidationError("手机号已存在")

        """ 发短信注册验证码 """
        code = random.randrange(1000, 10000)
        sms = send_sms_single(mobile_phone, template_id, [code, ])
        if sms["result"] != 0:
            raise ValidationError("短信发送失败，{}".format(sms["errmsg"]))

        """ 短信验证码写入 redis"""
        # conn = get_redis_connection()
        # conn.set(mobile_phone, code, ex=60)

        return mobile_phone
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : tencent_sms.py
__time__    : 2020/6/25 23:40
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from djangopy import settings


def send_sms_single(phone_num, template_id, template_param_list):
    """
    单条发送短信
    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表，例如：【验证码：{1}，描述：{2}】
    :return:
    """
    #应用 ID
    appid = settings.TENCENT_SMS_APP_ID
    # 应用 key
    appkey = settings.TENCENT_SMS_APP_KEY
    # 创建腾讯云创建签名时填写的签名内容
    sms_sign = settings.TENCENT_SMS_SIGN

    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(
            86,
            phone_num,
            template_id,
            template_param_list,
            sms_sign
        )
    except HTTPError as e:
        response = {
            "result": 1000,
            "errmsg": "网络异常发送失败"
        }
    return response

def send_sms_multi(phone_num_list, template_id, param_list):
    """
    批量发送短信
    :param phone_num_list:
    :param template_id:
    :param param_list:
    :return:
    """
    #应用 ID
    appid = 1400367199
    # 应用 key
    appkey = "43d2c318088e57f4141f5b190da0f577"
    # 创建腾讯云创建签名时填写的签名内容
    sms_sign = "DeepHub"

    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(
            86,
            phone_num_list,
            template_id,
            param_list,
            sms_sign
        )
    except HTTPError as e:
        response = {
            "result": 1000,
            "errmsg": "网络异常发送失败"
        }
    return response


if __name__ == '__main__':
    single_result = send_sms_single(
        phone_num="17729291319",
        template_id=601610,
        template_param_list=[523467, 5]
    )
    print(single_result)
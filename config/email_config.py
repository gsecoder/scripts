#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : email_config.py
__time__    : 2020/6/7 18:30
__author__  : crisimple
__github__ :  https://crisimple.github.io/
    python 邮件发送配置
"""

import smtplib
from email.mime.text import MIMEText
from util.read_ini import ReadIni

class EmailConfig(object):

    def __init__(self):
        # 读取邮箱服务端配置信息
        self.ri = ReadIni(ini_file="../data/email.ini")
        self.send_user = self.ri.read_ini("email_config", "send_user")
        self.mail_host = self.ri.read_ini("email_config", "mail_host")
        self.mail_passwd = self.ri.read_ini("email_config", "mail_passwd")
        print("self.send_user: ", self.send_user)
        print("self.mail_host: ", self.mail_host)
        print("self.mail_passwd: ", self.mail_passwd)

    def send_config(self, user_lists, subject, content):
        user = "发件人昵称" + "<" + self.send_user + ">"
        message = MIMEText(
            content,
            _subtype="plain",
            _charset="utf-8"
        )
        message["Subject"] = subject
        message["From"] = user
        message["To"] = "".join(user_lists)

        mail_server = smtplib.SMTP()
        mail_server.connect(self.mail_host)
        mail_server.login(self.send_user, self.mail_passwd)
        mail_server.sendmail(
            user,
            user_lists,
            message.as_string()
        )
        mail_server.close()

    def send_mail(self, msg):
        self.send_config(
            user_lists=['crisimple@qq.com'],
            subject="【邮件配置调试】",
            content=msg
        )


if __name__ == "__main__":
    ec = EmailConfig()
    ec.send_mail(
        "pass"
    )
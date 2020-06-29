#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : send_email.py
__time__    : 2020/6/29 22:50
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

from email.mime.multipart import MIMEMultipart  # 一封邮件
from email.mime.text import MIMEText    # 邮件内容
from email.mime.image import MIMEImage  # 图片
from email.mime.application import MIMEApplication  # 附件

import smtplib  # 发送邮件

"""
    准备发送邮件的参数
"""
# 发送人
sender = "crisimple@163.com"
# 收件人
to_list = [
    'crisimple@qq.com',
]
# 抄送人
cc_list = [
    'crisimple@hotmail.com'
]
subject = "【主题】这是邮件的主题"
# 授权码
auth_passwd = "wySmtp159357"

"""
    写邮件
"""
# 创建邮件
em = MIMEMultipart()    # em 是 message.Message 的一个字类对象
em["Subject"] = subject
em["From"] = sender
em["To"] = ",".join(to_list)
em["Cc"] = ",".join(cc_list)

# 邮件内容
# 发送带 html 图片的邮件
img = MIMEImage(open("dist/sql.png", mode="rb").read())  # 读取本地图片
img.add_header("Content-ID", "sql_img")     # 给图片设置id，让服务器知道要发送那张图片
em.attach(img)
# 发送附件
app = MIMEApplication(open('dist/sql.png', mode='rb').read())    # 读取要发送的附件
app.add_header('content-disposition', 'attachment', filename='这是附件名会更改的.mp4')
em.attach(app)
content = MIMEText(
    "<h3>这是我的邮件内容</h3><a href='www.360.cn'><img src='cid: sql_img'/></a>",
    _subtype="html")
em.attach(content)


"""
    发送邮件
"""
# 连接上邮件服务器的地址
smtp = smtplib.SMTP()
smtp.connect("smtp.163.com")
# 登陆
smtp.login(sender, auth_passwd)
# 发送邮件
smtp.send_message(em)
# 关闭连接
smtp.close()
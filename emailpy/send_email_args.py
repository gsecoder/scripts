#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
__file__    : send_email_args.py
__time__    : 2020/6/29 22:50
__author__  : crisimple
__github__ :  https://crisimple.github.io/
"""

from email.mime.multipart import MIMEMultipart  # 一封邮件
from email.mime.text import MIMEText    # 邮件内容
from email.mime.image import MIMEImage  # 图片
from email.mime.application import MIMEApplication  # 附件

import smtplib  # 发送邮件
# 另一个邮件模块import yagmail

"""
    import argparse
    # 创建对象
    parser = argparse.ArgumentParser()
    # 给定规则（两种用一种即可）
    # 2.1 位置参数
    parser.add_argument('a')
    parser.add_argument('b')
    # 2.2 指令参数
    parser.add_argument('a')
    parser.add_argument('-a', dest='par_a', nargs='+', default="会自动给默认值")   # default 不给 -a 的时候生效
    parser.add_argument('-b', dest='par_b', nargs='+', type=int, default=2, required=True)  # required -b 传参必须有不然报错
    parser.add_argument('-c', dest='par_c', action='store_true',default=False)  # action 实现参数的存在即满足-cde == -c -d -e
    parser.add_argument('-d', dest='par_d', action='store_true',default=False)  # required -b 传参必须有不然报错
    parser.add_argument('-e', dest='par_e', action='store_true',default=False)  # required -b 传参必须有不然报错
    parser.add_argument('-v', '--version', dest='version', action='store_true', default='3.8.1')
    # 解析 sys.argv（固定的）
    result = parser.parse_args()
    # 从解析的结果中拿到数据
    print("par_a: ", result.par_a)
    print("par_b: ", result.par_b)
    if result.version:
        print('3.8.1')
    else:
        print('None')
"""

"""
发送邮件参数列表
    sender: -s --sender 
    to_list: -t --to_list 多个
    cc_list: -c --cc_list 多个
    subject: -sub --subject 
    auth_passwd: -p --auth_passwd 
    smtp_server: -server --smtp_server 可选
"""
import argparse
parse = argparse.ArgumentParser()
parse.add_argument('-s', '--sender', dest='sender', required=True, help="发件人")
parse.add_argument('-t', '--to_list', dest='to_list', nargs='+', required=True, help="收件人")
parse.add_argument('-c', '--cc_list', dest='cc_list', default=[], nargs='*', required=False, help="抄送人")
parse.add_argument('-sub', '--subject', dest='subject', required=True, help="主题")
parse.add_argument('-p', '--auth_passwd', dest='auth_passwd', required=True, help="邮件服务器密码")
parse.add_argument('-server', '--smtp_server', dest='smtp_server', required=False, help="邮件服务器地址")
result = parse.parse_args()



"""
    准备发送邮件的参数
    未打包前通过执行程序传参发送邮件 
        python send_email_args.py -s crisimple@163.com -t crisimple@qq.com -sub TestArgsSub -p wySmtp159357
    打包程序成为一个可执行文件，直接利用命令完成脚本的调用
        pip install pyinstaller
        # glance
        打包程序：注意生成打包程序的执行路径
            ./dist/email.exe -s crisimple@163.com -t crisimple@qq.com -sub TestArgsSub -p wySmtp159357
"""
# 发送人
sender = result.sender
# 收件人
to_list = result.to_list
# 抄送人
cc_list = result.cc_list
subject = result.subject
# 授权码 "wySmtp159357"
auth_passwd = result.auth_passwd
# 邮箱服务器地址
smtp_server_dict = {
    "qq": "smtp.qq.com",
    "163": "smtp.163.com"
}
if not result.smtp_server:
    k = sender.split('@')[1].split('.')[0]
    v = smtp_server_dict.get(k)
    if v:
        smtp_server = v
    else:
        raise Exception("你的发件邮箱对应的邮件服务器不存在，请联系管理员！")
else:
    smtp_server = result.smtp_server

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
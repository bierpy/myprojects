#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/12 13:05
# @Author  : chenshoubiao
# @File    : sendmail.py


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def sendmail():
    ret = False
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["bier", 'biergogo@126.com'])
        msg['To'] = formataddr(["运动", '2784388828@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.126.com", 25)
        server.login("66666666@126.com", "邮箱密码")
        server.sendmail('biergogo@126.com', ['888888888@qq.com', ], msg.as_string())
        server.quit()
        print("发送成功")
    except Exception:
        print("发送失败")
        return ret

sendmail()



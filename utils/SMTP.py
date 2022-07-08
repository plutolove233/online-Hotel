#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:SMTP.py
# author:刘浩宇
# datetime: 2022/6/9 15:11
# software: PyCharm

"""
This is function description
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from utils.response_code import RET

sender = "1580916438@qq.com"
password = "wujzfnfvncmdjbbj"
port = 465


def send_email(receiver, verify_code):
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", port)
    message = f'修改密码的邮箱验证码为{verify_code}, 有效期为10分钟'
    message = MIMEText(message, 'plain', 'utf-8')
    message['From'] = Header('OnlineHotel', 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header('验证码验证', 'utf-8')
    try:

        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receiver, message.as_string())
        return {
            "code": RET.OK,
            "message":"send success",
        }
    except smtplib.SMTPException as e:
        print(str(e))
        return {
            "code": RET.INTERNALERR,
            "message": "send failed",
            "error": str(e),
        }
    finally:
        smtpObj.quit()

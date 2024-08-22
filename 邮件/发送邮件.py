# -*- coding: utf-8 -*-
__author__ = 'luointo'

import smtplib
from email.mime.text import MIMEText
from email.header import Header

"""
发送邮件

# MIMEMultipart的可选类型
MIMEMultipart（‘mixed’）       # 如果一封邮件中含有附件
MIMEMultipart(‘alternative’)  # 可以传送超文本内容，但出于兼容性的考虑，一般在发送超文本格式内容的同时会同时发送一个纯文本内容的副本
MIMEMultipart(‘related’)      # 除了可以携带各种附件外，还可以将其它内容以内嵌资源的方式存储在邮件中

MIMEMultipart类型
MIME邮件中各种不同类型的内容是分段存储的，各个段的排列方式、位置信息都通过Content-Type域的multipart类型来定义。multipart类型主要有三种子类型：mixed、alternative、related。
（1） MIMEMultipart类型基本格式
● MIMEMultipart（‘mixed’）类型
如果一封邮件中含有附件，那邮件的中必须定义multipart/mixed类型，邮件通过multipart/mixed类型中定义的boundary标识将附件内容同邮件其它内容分成不同的段。基本格式如下：
msg=MIMEMultipart(‘mixed’)

● MIMEMultipart(‘alternative’)类型
MIME邮件可以传送超文本内容，但出于兼容性的考虑，一般在发送超文本格式内容的同时会同时发送一个纯文本内容的副本，如果邮件中同时存在纯文本和超文本内容，则邮件需要在Content-Type域中定义multipart/alternative类型，邮件通过其boundary中的分段标识将纯文本、超文本和邮件的其它内容分成不同的段。基本格式如下：
msg=MIMEMultipart(‘alternative’)

● MIMEMultipart(‘related’)类型
MIME邮件中除了可以携带各种附件外，还可以将其它内容以内嵌资源的方式存储在邮件中。比如我们在发送html格式的邮件内容时，可能使用图像作为 html的背景，html文本会被存储在alternative段中，而作为背景的图像则会存储在multipart/related类型定义的段中。基本格式如下：
msg=MIMEMultipart(‘related’)

"""

subject = "邮件标题"  # 邮件的主题
# content = "邮件内容"  # 邮件的内容
smtp_server = 'smtp.163.com'
sender = "luointo@163.com"  # 发件人
password = "MMMHICQOQPDYHMAF"  # 邮箱授权密码
receiver = "277692343@qq.com"  # 收件人

# text文本格式邮件
# message = MIMEText("纯文本邮件", "plain", "utf-8")  # 发送的内容,内容的格式类型(plain与html),内容的编码方式

# html格式邮件
content = '<h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>'
message = MIMEText(content, "html", "utf-8")

message["From"] = sender  # 发送邮箱
message["To"] = receiver  # 接收邮箱
# message["Subject"] = subject  # 邮件标题
message['Subject'] = Header(subject, 'utf-8')  # subject

smtp = smtplib.SMTP(smtp_server, 25)  # SMTP：普通的邮件发送形式
# smtp = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP_SSL：QQ邮箱的SMTP服务器（端口465或587）
smtp.set_debuglevel(1)  # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
smtp.login(sender, password)  # 登录SMTP服务器，输入发送邮箱和密码
smtp.sendmail(sender, receiver, message.as_string())
smtp.quit()
smtp.close()

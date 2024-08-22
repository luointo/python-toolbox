# -*- coding: utf-8 -*-
__author__ = 'luointo'

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

"""
发送文本中带图片的邮件
"""

subject = "图片邮件测试"  # 邮件的主题
content = """<p>Python 邮件发送测试...</p><p><img src="cid:image1"></p>"""
smtp_server = 'smtp.163.com'
sender = "luointo@163.com"  # 发件人
password = "MMMHICQOQPDYHMAF"  # 邮箱授权密码
receiver = "277692343@qq.com"  # 收件人

message = MIMEMultipart("related")  # 构造一个MIMEMultipart对象代表邮件本身。related 表示使用内嵌资源的形式 将邮件发送给对方
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject

# msgAlternative = MIMEMultipart('alternative')               # 接收者的别名
# msgAlternative.attach(MIMEText(content, 'html', 'utf-8'))   # 添加文本
# message.attach(msgAlternative)
message.attach(MIMEText(content, 'html', 'utf-8'))  # 一步到位，不用上面三行代码

# ---------------发送图片的第一种方式-----------------------
with open('img.jpg', 'rb') as fp:  # 二进制模式读取图片
    msgImage = MIMEImage(fp.read())
msgImage.add_header("Content-ID", "<image1>")  # 定义图片ID，在HTML文本中引用
message.attach(msgImage)  # 添加图片到邮箱信息中去

# ---------------发送图片的第二种方式-----------------------
# msgImage = MIMEText(open('img.jpg', 'rb').read(), 'base64', 'utf-8')
# msgImage['Content-disposition'] = 'attachment;filename="happy.png"'
# message.attach(msgImage)


smtp = smtplib.SMTP_SSL(smtp_server, 465)
smtp.set_debuglevel(1)
smtp.login(sender, password)
try:
    smtp.sendmail(sender, receiver, message.as_string())
    smtp.quit()
    smtp.close()
except Exception as e:
    print("邮件发送失败,错误原因[{0}]".format(str(e)))
print("邮件发送成功")

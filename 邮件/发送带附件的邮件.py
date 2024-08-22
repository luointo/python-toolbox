# -*- coding: utf-8 -*-
__author__ = 'luointo'

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

"""
发送带附件的邮件
"""

subject = "附件邮件测试"  # 邮件的主题
content = "Python 邮件发送测试..."
smtp_server = 'smtp.163.com'
sender = "luointo@163.com"  # 发件人
password = "MMMHICQOQPDYHMAF"  # 邮箱授权密码
receiver = "277692343@qq.com"  # 收件人

message = MIMEMultipart("related")  # 构造一个MIMEMultipart对象代表邮件本身。related 表示使用内嵌资源的形式 将邮件发送给对方
message["From"] = sender
message["To"] = receiver
message["Subject"] = Header(subject, 'utf-8')
message.attach(MIMEText(content, 'html', 'utf-8'))  # 发送文本内容

# ---------------构造附件（文本或图片都行，文本用MIMEText，图片用MIMEText与MIMEImage都行）-----------------------
# att1 = MIMEImage(open(r'img.jpg', 'rb').read())
att1 = MIMEText(open(r'img.jpg', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# att1['Content-Disposition'] = 'attachment; filename="happy.jpg"'  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1.add_header('Content-Disposition', 'attachment', filename=Header("测试图片.jpg", 'utf-8').encode())
message.attach(att1)

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

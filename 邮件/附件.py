# -*- coding: utf-8 -*-
__author__ = 'luointo'

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

msg = MIMEMultipart()
msg['Subject'] = "标题"  # 标题
msg['From'] = ''  # 邮件中显示的发件人别称
msg['To'] = ''  # ...收件人...

# 正文-图片 只能通过html格式来放图片，所以要注释25，26行
mail_msg = '''
<p>\n\t this is auto test report!</p>
<p>\n\t you don't need to follow</p>
<p>截图如下：</p>
<p><img src="cid:image1"></p>
'''

msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))
# 指定图片为当前目录
fp = open(r'img.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# 附件-图片
image = MIMEImage(open(r'111.jpg', 'rb').read(), _subtype='octet-stream')
image.add_header('Content-Disposition', 'attachment', filename='img.jpg')
msg.attach(image)

# 附件-文件
file = MIMEBase('application', 'octet-stream')
file.set_payload(open(r'320k.txt', 'rb').read())
file.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '测试.txt'))
encoders.encode_base64(file)
msg.attach(file)

# 构造附件
att = MIMEText(open('/Users/1.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="1.jpg"'
msg.attach(att)

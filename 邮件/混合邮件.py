# -*- coding: utf-8 -*-
__author__ = 'luointo'

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

receiver = '***'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = '***'
password = '***'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('mixed')
msg['Subject'] = "Link"

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\

Hi!

 How are you?

 Here is the link you wanted.

"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# 构造附件
att = MIMEText(open('/Users/1.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="1.jpg"'
msg.attach(att)

# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(username, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()

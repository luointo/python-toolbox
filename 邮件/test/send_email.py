# -*- coding: utf-8 -*-
__author__ = 'luointo'

import csv
import eml_parser
import smtplib
import base64
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.header import Header
from pathlib import Path

# 群发的来源文件
source_file = "D:\Desktop\email\邮件群发.csv"

# where=1 邮件内容为html且有一张图片
# where=2 邮件内容为text且无附件
where = 1

eml_filename = "email.eml"  # eml文件路径
# eml_filename = "test.eml"  # eml文件路径

# 发件人
sender = 'luointo@163.com'

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "luointo@163.com"  # 用户名
mail_pass = "MMMHICQOQPDYHMAF"  # 口令

source_list = []
try:
    with open(file=source_file, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if reader.line_num == 1:
                continue
            dic = {
                "to": row[0],
                "cc": row[1],
                "file": row[2],
            }
            source_list.append(dic)
except Exception as e:
    print("群发来源文件解析错误:%s", e)
    exit()


def get_eml_parsed(filename):
    with open(filename, 'rb') as f:
        raw_email = f.read()
        ep = eml_parser.EmlParser()
        ep.include_raw_body = True
        ep.include_attachment_data = True
        return ep.decode_email_bytes(raw_email)


content = None
subject = None
img_raw = None
img_cid = None

if where == 1:
    parsed_eml = get_eml_parsed(eml_filename)
    header = parsed_eml['header']
    # for k, v in parsed_eml.items():
    #     print(k, v)
    # exit()
    attachment = parsed_eml['attachment']
    if not isinstance(attachment, list):
        print("html资源未知")
        exit()
    attachment_one = attachment[0]
    if attachment_one['extension'] != "jpg":
        print("未找到jpg图片")
        exit()
    img_raw = attachment_one['raw']
    img_raw = base64.b64decode(img_raw)
    # for k, v in attachment_one.items():
    #     print(k, v)
    img_cid = attachment_one['content_header']['content-id'][0]
    # print(img_cid)
    # exit()
    body = parsed_eml['body']
    for data in body:
        if data["content_type"] == "text/html":
            content = data['content']
            break
    if content is None:
        print("获取内容失败")
        exit()
    # msg['Subject'] = header['subject']  # 邮件标题
    # msg.attach(MIMEText(content, 'html', 'utf-8'))
    # msg_image = MIMEImage(img_raw)
    # msg_image.add_header('Content-ID', img_cid)
    # msg.attach(msg_image)
    # msg['From'] = sender
    subject = header['subject']

elif where == 2:
    parsed_eml = get_eml_parsed(eml_filename)
    header = parsed_eml['header']
    body = parsed_eml['body']
    for data in body:
        if data["content_type"] == "text/plain":
            content = data['content']
            break
    if content is None:
        print("获取内容失败")
        exit()
    subject = header['subject']

else:
    print("请先配置where条件")
    exit()

msg_list = []
to_list = []
cc_list = []
receiver_list = []  # 接收邮件
for source in source_list:
    filepath = source['file']
    p = Path(filepath)
    if not p.exists():
        print("文件:{} 不存在".format(p))
        exit()
    to = source['to']
    cc = source['cc']
    to_list.append(to)
    cc_list.append(cc)

    msg = MIMEMultipart('related')
    if where == 1:
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        msg_image = MIMEImage(img_raw)
        msg_image.add_header('Content-ID', img_cid)
        msg.attach(msg_image)

    elif where == 2:
        add_body = MIMEText(content, _subtype='plain', _charset='utf_8')  # 设置邮件正文内容
        msg.attach(add_body)  # 将正文添加到邮件中
    msg['From'] = sender
    msg['To'] = to
    msg['Cc'] = cc
    msg['Subject'] = subject
    filename = p.name

    # 添加附件
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(p.open("rb").read())
    # att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', filename))  # 防止中文乱码，二选一
    att.add_header('Content-Disposition', 'attachment', filename=Header(filename, 'utf-8').encode())
    encoders.encode_base64(att)
    msg.attach(att)
    msg_list.append(msg)

receiver_list = to_list + cc_list
receiver_list = list(set(receiver_list))


def send_mail(message):
    # 发送邮件
    try:
        # smtp = smtplib.SMTP_SSL(mail_host, 465)
        # smtp.login(mail_user, mail_pass)
        # smtp.sendmail(sender, receiver_list, message.as_string())

        smtp = smtplib.SMTP(mail_host, 25)
        smtp.connect(mail_host)
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(sender, receiver_list, message.as_string())
        # print('success')
        smtp.quit()
    except smtplib.SMTPException as err:
        print('error', err)
        exit()


i = 1
for msg in msg_list:
    send_mail(msg)
    print(f"第{i}封, To:{msg['To']} Cc:{msg['Cc']}")
    i += 1
    time.sleep(0.3)

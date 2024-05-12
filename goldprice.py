import datetime

import requests

url='https://www.huilvbiao.com/gold/indexApi'
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
}

response=requests.get(url=url,headers=headers)

str=response.text

price=str.split('\n')
price[0]=price[0].replace("var hq_str_gds_AUTD=","").strip('"')
price[1]=price[1].replace("var hq_str_hf_GC=","").strip('"')
price[2]=price[2].replace("var hq_str_hf_XAU=","").strip('"')
China_gold=price[0].split(',')[0]#人名币/克
USA_gold=price[1].split(',')[0]#美元/蛊司
UK_gold=price[2].split(',')[0]#美元/蛊司
China_gold=eval(China_gold)
USA_gold=eval(USA_gold)
UK_gold=eval(UK_gold)

#1 盎司 = 31.1034768 克
oz_ounce=31.1034768

rateUrl="https://assets.msn.cn/service/Finance/Quotes?apikey=0QfOX3Vn51YCzitbLaRkTTBadtWpgTN8NZLW0C1SEM&activityId=90AF134C-E6E2-49DD-B9EF-F96A88FAA3D6&ocid=finance-utils-peregrine&cm=zh-cn&it=edgeid&scn=APP_ANON&ids=avym77,av554c,avybkr,avdzk2,av8u5r,avyomw,av4yk2,avyn9c,avbknm,auxj9c,av932w,av4xw7,av3onm,av4yvh,avyjhw,ad88mw,adfh77,ad87qh,auvwoc,adg1m7,ad9b1h,ah7etc,a6qja2,adci1h,ad99yc,adf7ec,avyu4c,avylur,avykh7,avynz2,avyo8m,avys2w,avyoyc&wrapodata=false"

rateHeaders={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
}

rateResponse=requests.get(url=rateUrl,headers=rateHeaders)
tempdata=rateResponse.text.strip('[').strip(']').strip('{').strip('}')
rate=tempdata.split(',')

currate=rate[0].replace('"price":','')
rateDayHigh=rate[2].replace('"priceDayHigh":','')
rateDayLow=rate[3].replace('"priceDayLow":','')
currate=eval(currate)
#rateDayHigh=eval(rateDayHigh)
#rateDayLow=eval(rateDayLow)


China=China_gold
USA=USA_gold/oz_ounce*currate
UK=UK_gold/oz_ounce*currate

curtime="时间为："+datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')+'\n'

text=curtime+"此时黄金价格如下"+'\n'+f"国内黄金价格：{China}"+'\n'+f"纽约期货国际金价：{USA}"+'\n'+f"伦敦现货黄金价格：{UK}"
Rate="当日汇率(1美元兑人民币)"+'\n'+f"此刻汇率：{currate}"+'\n'+f"当日最高汇率：{rateDayHigh}"+'\n'+f"当日最低汇率：{rateDayLow}"

print(text)
print()
print(Rate)

fp=open('C:\\Users\\ASUS\\Desktop\\goldprice.txt','a',encoding='utf-8')
fp.write(text+'\n'+'\n'+Rate+'\n'+'\n'+'\n')
fp.close()

# 使用 smtplib 模块发送纯文本邮件
import smtplib
import ssl
from email.message import EmailMessage

EMAIL_ADDRESS = "xghxgh200505275416@163.com"  # 邮箱的地址
EMAIL_PASSWORD = "DAGZULCEYALZWWOG"  # 授权码

# 也可以使用ssl模块的context加载系统允许的证书，在登录时进行验证
context = ssl.create_default_context()

subject = "今日黄金价格"
body = text+'\n'+'\n'+Rate

msg = EmailMessage()
msg['subject'] = subject  # 邮件标题
msg['From'] = EMAIL_ADDRESS  # 邮件发件人
msg['To'] = "xgh200505275416@163.com"  # 邮件的收件人ggg111090@163.com
msg.set_content(body)  # 使用set_content()方法设置邮件的主体内容

with smtplib.SMTP_SSL("smtp.163.com", 465, context=context) as smtp:  # 完成加密通讯

    # 连接成功后使用login方法登录自己的邮箱
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


#发送给不同人
context = ssl.create_default_context()

subject = "今日黄金价格"
body = text+'\n'+'\n'+Rate

msg = EmailMessage()
msg['subject'] = subject  # 邮件标题
msg['From'] = EMAIL_ADDRESS  # 邮件发件人
msg['To'] = "13225864238@163.com"  # 邮件的收件人ggg111090@163.com
msg.set_content(body)  # 使用set_content()方法设置邮件的主体内容

with smtplib.SMTP_SSL("smtp.163.com", 465, context=context) as smtp:  # 完成加密通讯

    # 连接成功后使用login方法登录自己的邮箱
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)


#发送给不同人
context = ssl.create_default_context()

subject = "今日黄金价格"
body = text+'\n'+'\n'+Rate

msg = EmailMessage()
msg['subject'] = subject  # 邮件标题
msg['From'] = EMAIL_ADDRESS  # 邮件发件人
msg['To'] = "15955922051@163.com"  # 邮件的收件人ggg111090@163.com
msg.set_content(body)  # 使用set_content()方法设置邮件的主体内容

with smtplib.SMTP_SSL("smtp.163.com", 465, context=context) as smtp:  # 完成加密通讯

    # 连接成功后使用login方法登录自己的邮箱
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)







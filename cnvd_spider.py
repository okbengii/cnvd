# coding:utf-8

import requests
import re
import time
import datetime
s1 = "2018-01-02"
s2 = "02-19"
pattern = "[0-9]*?-[0-9]*?-[0-9]*?"
now_time = time.strptime(s1, "%Y-%m-%d")
y,m,d,h,mm,s = now_time[0:6]
update_time = datetime.datetime(y,m,d,h,mm,s)
headers = {
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
	"Origin": "http://www.cnvd.org.cn",
	"Host": "www.cnvd.org.cn",
	"Referer": "http://www.cnvd.org.cn/flaw/list.htm?flag=true"
}

cookies = {
	"__jsluid":"d65b87350a0e5bad323c196df0e25a9b",
	"bdshare_firstime":"1521101814429",
	"__jsl_clearance":"1521101810.895|0|Fvf6g18AZQkeznGdRNQmS6WzbTg%3D",
	"JSESSIONID":"98F485BD5B2C632C2BBC9D58A1E5E8F5"
}

params = {
	"number":u"请输入精确编号",
	"startDate":"",
	"endDate":"",
	"field":"",
	"flag":"true",
	"max":"20",
	"order":"",
	"offset":"40"
	}

url = "http://www.cnvd.org.cn/flaw/list.htm?flag=true"
content = requests.post(url,headers=headers,data=params,cookies=cookies)

print content.content

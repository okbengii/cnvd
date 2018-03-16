# coding:utf-8

import requests
import re
import time
import datetime
from selenium import webdriver


def getCookie():
        spiderFirefox = webdriver.Firefox()
        spiderFirefox.get("http://www.cnvd.org.cn/")
        time.sleep(5)
        cookies = ""
        for cookie in spiderFirefox.get_cookies():
            cookies += u"%s=%s; "%(cookie["name"], cookie["value"])
        spiderFirefox.close()
        return cookies
Cookies = getCookie()
print Cookies
headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0",
            "Referer":"http://www.cnvd.org.cn/",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cookie":Cookies,
            "Host":"www.cnvd.org.cn",
            "Cache-Control":"no-cache",
            "Pragma":"no-cache",
            "Connection":"keep-alive"
        }
url = "http://www.cnvd.org.cn/"
content = requests.get(url,headers=headers)

print content.content

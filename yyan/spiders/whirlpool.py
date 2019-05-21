# -*- coding: utf-8 -*-

import os
import urllib
import requests
from lxml import html
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from multiprocessing.pool import ThreadPool

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Header
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

for page in range(1000, 1001):
    url = 'https://forums.whirlpool.net.au/user/%s' % page
    # print(url)
    response = requests.get(url, timeout=5, headers=HEADERS).text
    selector = html.fromstring(response)
    # print(html.tostring(selector))
    # User Name
    uname = selector.xpath('//ul[@class="breadcrumb"]/li[2]/span/text()')[0]
    uname = (uname.split(" (")[0])

    # User Status
    status = selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[1]/td[2]/text()')[0]
    status = status.split("\r")[0]

    # User Hardware Or City
    x = 2
    if "Network hardware:" == selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[2]/td[1]/b/text()')[0]:
        print("yes")
    else:
        print("Np")




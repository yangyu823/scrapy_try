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

for page in range(84000, 84001):
    url = 'https://forums.whirlpool.net.au/user/%s' % page
    # print(url)
    response = requests.get(url, timeout=5, headers=HEADERS).text
    selector = html.fromstring(response)
    # print(html.tostring(selector))
    # User Name
    uname = selector.xpath('//ul[@class="breadcrumb"]/li[2]/span/text()')[0]
    uname = (uname.split(" (")[0])

    tr_size = len(selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr'))
    i = 1
    while i <= tr_size:
        tagname = \
            (selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[1]/b/text()' % i)[0]).split(":")[0]
        if tagname == "Whim":
            tagdata = (selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/a/text()' % i)[0])
        else:
            tagdata = (selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/text()' % i)[0]).split("\r")[0]


        print(tagname, ":", tagdata)
        i += 1

    # print(tr_size)

    # # User Status
    # status = selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[1]/td[2]/text()')[0]
    # status = status.split("\r")[0]
    #
    # # User Hardware Or City
    # x = 2
    # if "Network hardware:" == selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[2]/td[1]/b/text()')[0]:
    #     hw_size = (len(selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[2]/td[2]/a')))
    #     i = 0
    #     hw_name_list = []
    #     while i < hw_size:
    #         hw_name = selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[2]/td[2]/a/text()')[i]
    #         i += 1
    #         hw_name_list.append(hw_name)
    #     x += 1
    #     print(hw_name_list, x)
    #
    # city = selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[1]/td[2]/text()')[0]

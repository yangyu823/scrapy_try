# -*- coding: utf-8 -*-

import os
import urllib
import requests
from lxml import html
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from multiprocessing.pool import ThreadPool
import json
import csv
from tqdm import tqdm

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Header
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}
ulist = []

os.system("clear")

for page in tqdm(range(1000, 1500), desc="Data Store"):
    url = 'https://forums.whirlpool.net.au/user/%s' % page
    # print(url)
    response = requests.get(url, timeout=5, headers=HEADERS).text
    selector = html.fromstring(response)
    # print(html.tostring(selector))
    # User Name
    uname = (selector.xpath('//ul[@class="breadcrumb"]/li[2]/span/text()')[0]).split(" (")[0]

    # print(uname)
    user = {"User_Name": uname}
    tr_size = len(selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr'))
    # print(tr_size)
    i = 1
    while i <= tr_size:
        tagname = \
            (selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[1]/b/text()' % i)[0]).split(":")[0]
        if tagname == "Whim":
            tagdata = (selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/a/text()' % i)[0])
        elif tagname == "Aura":
            tagdata = \
                ((selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/text()' % i)[
                    0]).strip()).split("\r")[0]
        elif tagname == "Network hardware":
            hw_size = len(selector.xpath('//*[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/a' % i))
            m = 1
            tagdata = []
            while m <= hw_size:
                tagdata.append(selector.xpath('//*[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/a/text()' % i)[0])
                m += 1
        else:
            tagdata = \
                (selector.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/text()' % i)[0]).split("\r")[
                    0]

        user.update({tagname: tagdata})
        i += 1
    ulist.append(user)

    with open('data.json', 'w') as outfile:
        json.dump(ulist, outfile, indent=4, ensure_ascii=False)
    outfile.close()
    time.sleep(1.5)



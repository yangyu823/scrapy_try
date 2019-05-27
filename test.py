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

for page in tqdm(range(1000, 1001), desc="Data Store"):
    url = 'https://forums.whirlpool.net.au/user/%s' % page
    # print(url)
    response = requests.get(url, timeout=5, headers=HEADERS).text
    selector = html.fromstring(response)
    # print(html.tostring(selector))
    # User Name

    # if len(selector.xpath('//ul[@class="breadcrumb"]/li'))

    uname = (selector.xpath('//ul[@class="breadcrumb"]/li[2]/span/text()')[0]).split(" (")[0]


    # with open('error.html', 'w') as outfile:
    #     outfile.write(response)
    #     outfile.close()

    print(uname)

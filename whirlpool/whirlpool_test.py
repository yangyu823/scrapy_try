# -*- coding: utf-8 -*-
import os
import json
import csv
import time
import urllib
import random
import requests
from lxml import html
from tqdm import tqdm
from get_proxy import test
from itertools import cycle
from multiprocessing.pool import ThreadPool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# Header
user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]
rlist = []
ulist = []
index = 1100
# os.system("clear")
test()
with open('list_final.json') as infile:
    proxylist = (json.load(infile))
    infile.close()
proxy = random.choice(proxylist)
user_agent = random.choice(user_agent_list)

i = 0
while i < 10:
    print(random.choice(proxylist))
    i += 1


def get_data(sele):
    # User Name
    uname = (sele.xpath('//ul[@class="breadcrumb"]/li[2]/span/text()')[0]).split(" (")[0]

    # print(uname)
    user = {"User_Name": uname}
    tr_size = len(sele.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr'))
    # print(tr_size)
    i = 1
    while i <= tr_size:
        tagname = \
            (sele.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[1]/b/text()' % i)[0]).split(":")[0]
        if tagname == "Whim":
            tagdata = (sele.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/a/text()' % i)[0])
        elif tagname == "Aura":
            tagdata = \
                ((sele.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/text()' % i)[
                    0]).strip()).split("\r")[0]
        elif tagname == "Network hardware":
            hw_size = len(sele.xpath('//*[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/a' % i))
            m = 1
            tagdata = []
            while m <= hw_size:
                tagdata.append(sele.xpath('//*[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/a/text()' % i)[0])
                m += 1
        else:
            tagdata = \
                (sele.xpath('//div[@id="userprofile"]/div[2]/table/tbody/tr[%r]/td[2]/text()' % i)[0]).split("\r")[
                    0]

        user.update({tagname: tagdata})
        i += 1
    ulist.append(user)

    with open('data.json', 'w') as outfile:
        json.dump(ulist, outfile, indent=4, ensure_ascii=False)
    outfile.close()


if __name__ == '__main__':
    for page in tqdm(range(1000, index), desc="Data Store"):
        url = 'https://forums.whirlpool.net.au/user/%s' % page
        p = random.choice(proxylist)
        u = random.choice(user_agent_list)
        response = requests.get(url, timeout=5, headers={'User-Agent': u}, proxies={"https": p}).text
        selector = html.fromstring(response)

        if len(selector) < 3:
            rlist.append(page)
            # user_agent = random.choice(user_agent_list)
        else:
            get_data(selector)
    print(rlist)

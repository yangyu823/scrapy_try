# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 18:00
# @Author  : Liangjianghao
# @Email   : 1084933098@qq.com
# @Software: PyCharm
import os
import urllib
import requests
from lxml import html
import time
from multiprocessing import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import _thread
import json
from tqdm import tqdm

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if not os.path.exists("meizi"):
    os.mkdir("meizi")

for page in range(1, 2):
    url = 'http://www.mmonly.cc/mmtp/list_9_%s.html' % page
    # print(url)
    response = requests.get(url, verify=False).text
    selector = html.fromstring(response)
    imgEle = selector.xpath('//div[@class="ABox"]/a')
    # print(len(imgEle))

    total = 0
    imglink = {}

# print(enumerate(imgEle))
data = ((index, img.xpath('@href')) for index, img in enumerate(imgEle))


def getttt(ttt):
    # for index, img in tqdm(enumerate(imgEle), total=len(imgEle), desc="Extracting Image URL"):
    # print(ttt)
    index,img = ttt
    print(index)
    # imgUrl = img.xpath('@href')[0]
    # response = requests.get(imgUrl, verify=False).text
    # selector = html.fromstring(response)
    # pageEle = selector.xpath('//div[@class="wrapper clearfix imgtitle"]/h1/span/span[2]/text()')[0]
    # # print(pageEle)
    # # total += int(pageEle)
    #
    # imgE = selector.xpath('//a[@class="down-btn"]/@href')[0]
    # # print(imgE)
    # imgName = '%s_%s_1.jpg' % (page, str(index + 1))
    # coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)
    # # urllib.request.urlretrieve(imgE, coverPath)
    # imglink.update({imgName: imgE})

    # time.sleep(2)
    # print("Total number of image save to file is %r" % total)


# i = 0
# with open("img.json", "w") as outfile:
#     json.dump(imglink, outfile, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    with tqdm(total=len(imgEle)) as t:
        for _ in Pool(20).imap_unordered(getttt, data):
            t.update(1)
    # Pool(20).join()

    # print(imglink)

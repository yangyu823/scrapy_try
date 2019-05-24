# -*- coding: utf-8 -*-
import os
import urllib
import requests
from lxml import html
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import _thread
import json
from multiprocessing import Pool
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
    data = ((index, img.xpath('@href')) for index, img in enumerate(imgEle))


def getlink(data):
    index, img = data
    imgUrl = img[0]
    # print(imgUrl)
    response = requests.get(imgUrl, verify=False).text
    selector = html.fromstring(response)
    pageEle = selector.xpath('//div[@class="wrapper clearfix imgtitle"]/h1/span/span[2]/text()')[0]
    # print(pageEle)

    imgE = selector.xpath('//a[@class="down-btn"]/@href')[0]
    # print(imgE)
    imgName = '%s_%s_1.jpg' % (page, str(index + 1))
    coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)
    urllib.request.urlretrieve(imgE, coverPath)
    # imglink.update({imgName: imgE})

    for page_2 in range(2, int(pageEle) + 1):
        url = imgUrl.replace('.html', '_%s.html' % str(page_2))
        response = requests.get(url).text
        selector = html.fromstring(response)
        imgEle = selector.xpath('//a[@class="down-btn"]/@href')[0]
        # print(imgEle)
        imgName = '%s_%s_%s.jpg' % (page, str(index + 1), page_2)
        coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)
        urllib.request.urlretrieve(imgEle, coverPath)
        # imglink.update({imgName: imgEle})
    # print(imglink)
    # return imglink

# print(imglink)

if __name__ == '__main__':
    with tqdm(total=len(imgEle)) as t:
        for _ in Pool(20).imap_unordered(getlink, data):
            t.update(1)
        # print(imglink)
        # with open("img.json", "w") as outfile:
        #     json.dump(imglink, outfile, indent=4, ensure_ascii=False)

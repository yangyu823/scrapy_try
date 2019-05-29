# -*- coding: utf-8 -*-
import os
import urllib
import requests
from lxml import html
from tqdm import tqdm
from multiprocessing import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if not os.path.exists("meizi"):
    os.mkdir("meizi")
default = 'http://www.mmonly.cc/mmtp/list_9_1.html'
response = requests.get(default, verify=False).text
selector = html.fromstring(response)
num = len(selector.xpath('//div[@id="pageNum"]/a'))
imgEle = selector.xpath('//div[@id="pageNum"]/a[%r]/@href' % num)[0]
totalPage = (((imgEle.split(".")[0]).split("_"))[-1])

for page in range(1, int(totalPage)):
    url = 'http://www.mmonly.cc/mmtp/list_9_%s.html' % page
    response = requests.get(url, verify=False).text
    selector = html.fromstring(response)
    imgEle = selector.xpath('//div[@class="ABox"]/a')
    data = ((index, img.xpath('@href')) for index, img in enumerate(imgEle))


    def getlink(temp):
        index, img = temp
        imgUrl = img[0]
        response = requests.get(imgUrl, verify=False).text
        selector = html.fromstring(response)
        pageEle = selector.xpath('//div[@class="wrapper clearfix imgtitle"]/h1/span/span[2]/text()')[0]

        imgE = selector.xpath('//a[@class="down-btn"]/@href')[0]
        imgName = '%s_%s_1.jpg' % (page, str(index + 1))
        coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)
        urllib.request.urlretrieve(imgE, coverPath)

        for page_2 in range(2, int(pageEle) + 1):
            url = imgUrl.replace('.html', '_%s.html' % str(page_2))
            response = requests.get(url).text
            selector = html.fromstring(response)
            imgEle = selector.xpath('//a[@class="down-btn"]/@href')[0]
            # print(imgEle)
            imgName = '%s_%s_%s.jpg' % (page, str(index + 1), page_2)
            coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)
            urllib.request.urlretrieve(imgEle, coverPath)


    if __name__ == '__main__':
        with tqdm(total=len(imgEle), desc="Page %r MeiZi" % page) as t:
            for _ in Pool(20).imap_unordered(getlink, data):
                t.update(1)

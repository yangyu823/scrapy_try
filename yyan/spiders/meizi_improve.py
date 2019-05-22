# -*- coding: utf-8 -*-
import os
import urllib
import requests
from lxml import html
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from tqdm import tqdm
from multiprocessing.pool import ThreadPool

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if not os.path.exists("meizi"):
    os.mkdir("meizi")

for page in tqdm(range(1, 3), desc="Page count"):
    url = 'http://www.mmonly.cc/mmtp/list_9_%s.html' % page
    # print(url)
    response = requests.get(url, verify=False).text

    selector = html.fromstring(response)
    imgEle = selector.xpath('//div[@class="ABox"]/a')
    # print(len(imgEle))
    total = 0

    for index, img in enumerate(imgEle):
        imgUrl = img.xpath('@href')[0]
        response = requests.get(imgUrl, verify=False).text
        selector = html.fromstring(response)
        pageEle = selector.xpath('//div[@class="wrapper clearfix imgtitle"]/h1/span/span[2]/text()')[0]
        # print(pageEle)
        total += int(pageEle)
        imgE = selector.xpath('//a[@class="down-btn"]/@href')[0]
        # print(imgE)
        imgName = '%s_%s_1.jpg' % (page, str(index + 1))
        coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)

        # Output 1st IMG to file
        urllib.request.urlretrieve(imgE, coverPath)

        temp = []
        for page_2 in range(2, int(pageEle) + 1):
            url = imgUrl.replace('.html', '_%s.html' % str(page_2))
            # print("page", page_2)
            temp.append(url)


        def get_subIMG(url):
            try:
                response = requests.get(url).text
                selector = html.fromstring(response)
                imgEle = selector.xpath('//a[@class="down-btn"]/@href')[0]
                fileEle = selector.xpath('//div[@class="wrapper clearfix imgtitle"]/h1/span/span[1]/text()')[0]
                # print(fileEle)
                imgName = '%s_%s_%s.jpg' % (page, str(index + 1), fileEle)
                coverPath = '%s/meizi/%s' % (os.getcwd(), imgName)
                # Output (2nd ~ Rest) IMG to file
                urllib.request.urlretrieve(imgEle, coverPath)
                # print("Image saved at %r" % (coverPath,))
                return url, None
            except Exception as e:
                return url, e


        results = ThreadPool(5).imap_unordered(get_subIMG, temp)
        # for url, error in results:
        #     if error is None:
        #         print(" Image URL is ", url)
        #     else:
        #         print("error fetching")

    time.sleep(2)
    print("Total Sum is %r" % (total,))

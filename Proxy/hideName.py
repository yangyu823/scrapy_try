# -*- coding: utf-8 -*-
import os
import json
import csv
import time
import urllib
import requests
import cookielib
from lxml import html
from tqdm import tqdm
from selenium import webdriver
from time import sleep
from multiprocessing.pool import ThreadPool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}


def get_data():
    url = 'https://hidemyna.me/en/proxy-list/?maxtime=1000&type=s#list'
    response = requests.get(url, timeout=5, headers=HEADERS).text
    selector = html.fromstring(response)
    # uname = (selector.xpath('//*[@class="proxy__t"]/tbody/tr[1]/td[1]/text()')[0])
    # length = len(selector.xpath('//*[@class="proxy__t"]/tbody/tr[1]/td[1]/text()'))
    length = len(selector.xpath('//*[@class="proxy__t"]'))

    print(length)


if __name__ == '__main__':
    get_data()

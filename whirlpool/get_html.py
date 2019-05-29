import json
import requests
from tqdm import tqdm
from multiprocessing.pool import ThreadPool
from itertools import cycle
from lxml.html import fromstring

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

#   http://spys.one/en/https-ssl-proxy/ #####
url = 'https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=100&country=all&ssl=all&anonymity=elite'
response = requests.get(url, timeout=5, headers=HEADERS).text
tempList = response.split('\r\n')[:-1]
print("###########    Update Source Proxy List")


# print(tempList)


def test_proxy():
    testUrl = 'https://httpbin.org/ip'
    for p in tqdm(tempList, desc='Clean Proxy List ...'):
        # print("Request #%s" % p)
        try:
            response = requests.get(testUrl, timeout=2, proxies={"http": p, "https": p})
            print(response.json())
        except:
            tempList.remove(p)
            print("Skipping. Connnection error")


if __name__ == '__main__':
    testUrl = 'https://httpbin.org/ip'
    try:
        requests.get(testUrl, timeout=2, proxies={"http": '39.96.210.247:8080', "https": '39.96.210.247:8080'})
        print(response.json())
    except:
        print("Skipping. Connnection error")

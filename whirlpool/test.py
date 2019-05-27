import requests
import base64
from itertools import cycle
from lxml.html import fromstring

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}


# https://free-proxy-list.net/  #####
def get_proxies():
    url = 'https://www.sslproxies.org/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:20]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    # print(proxies)
    return proxies


proxies = get_proxies()
# proxy_pool = cycle(proxies)

txt = requests.get("https://proxy.rudnkh.me/txt").text
tempList = (txt.split('\n')[:-1])


url = 'https://httpbin.org/ip'
# print(proxies)

if __name__ == '__main__':

    # for i in range(1, 11):
    # Get a proxy from the pool
    # proxy = next(proxy_pool)

    for p in tempList:
        # print("Request #%s" % p)
        try:
            response = requests.get(url, timeout=10, proxies={"http": p, "https": p})
            print(response.json())
        except:
            # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
            # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
            tempList.remove(p)
            print("Skipping. Connnection error")
print("############################################################")
print(tempList)

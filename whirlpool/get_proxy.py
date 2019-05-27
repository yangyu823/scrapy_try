import requests
from itertools import cycle
from lxml.html import fromstring


#   http://spys.one/en/https-ssl-proxy/ #####
def get_proxies():
    url = 'http://spys.one/en/https-ssl-proxy/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[4:33]:
        # //Setup for future speed node selection//
        # if i.xpath('.//td[7][contains(text(),"yes")]'):
            # Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    # print(proxies)
    return proxies


#   https://free-proxy-list.net/  #####
# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr')[:20]:
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             # Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     # print(proxies)
#     return proxies


proxies = get_proxies()
proxies = {}

proxy_pool = cycle(proxies)

url = 'https://httpbin.org/ip'
print(proxies)

if __name__ == '__main__':

    for i in range(1, 11):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(url, timeout=5, proxies={"http": proxy, "https": proxy})
            print(response.json())
        except:
            # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
            # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
            proxies.remove(proxy)
            print("Skipping. Connnection error")
print("############################################################")
print(proxies)

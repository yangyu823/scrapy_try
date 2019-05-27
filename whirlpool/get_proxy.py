import requests
from itertools import cycle
from lxml.html import fromstring

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}


#   http://spys.one/en/https-ssl-proxy/ #####
def get_proxies():
    url = 'http://spys.one/en/https-ssl-proxy/'
    response = requests.get(url, timeout=5, headers=HEADERS)
    parser = fromstring(response.text)
    proxies = set()

    # lens = len(parser.xpath('//body/table/tbody/tr[4]/td/table/tbody/tr'))
    lens = (parser.xpath('//body/table[2]/tr[4]/td/table/tr[4]/td[1]/font[2]/script/text()')[0])
    #
    print(lens)

    # for i in parser.xpath('//body/table[2]/tr[4]/td/table/tr')[3:33]:
    #     # //Setup for future speed node selection//
    #     # if i.xpath('.//td[7][contains(text(),"yes")]'):
    #
    #     # Grabbing IP and corresponding PORT
    #     proxy = i.xpath('.//td[1]/font[2]/text()')[0]
    #
    #     # proxy = ":".join([i.xpath('.//td[1]/font[2]/text()')[0], i.xpath('.//td[1]/font[2]/text()')[1]])
    #     proxies.add(proxy)
    #     print(proxy)
    # return proxies


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

# proxy_pool = cycle(proxies)

# url = 'https://httpbin.org/ip'
# print(proxies)

# if __name__ == '__main__':
#
#     for i in range(1, 11):
#         # Get a proxy from the pool
#         proxy = next(proxy_pool)
#         print("Request #%d" % i)
#         try:
#             response = requests.get(url, timeout=5, proxies={"http": proxy, "https": proxy})
#             print(response.json())
#         except:
#             # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
#             # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
#             proxies.remove(proxy)
#             print("Skipping. Connnection error")
print("############################################################")
# print(proxies)

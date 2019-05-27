import requests
from itertools import cycle
from lxml.html import fromstring

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}


#   http://spys.one/en/https-ssl-proxy/ #####
def get_proxies():
    url = 'http://spys.one/en/https-ssl-proxy/'
    response = requests.get(url, timeout=5, headers=HEADERS).text

    # parser = fromstring(response.text)




    with open('error.html', 'w') as outfile:
        outfile.write(response)
        outfile.close()
    proxies = set()


if __name__ == '__main__':
    get_proxies()
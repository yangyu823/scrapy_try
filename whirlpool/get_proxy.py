import requests
from tqdm import tqdm
from itertools import cycle
from lxml.html import fromstring

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

txt = requests.get("https://proxy.rudnkh.me/txt").text
tempList = (txt.split('\n')[:-1])
testUrl = 'https://httpbin.org/ip'


def get_list():
    for p in tqdm(tempList, desc='Clean Proxy List ...'):
        # print("Request #%s" % p)
        try:
            response = requests.get(testUrl, timeout=10, proxies={"http": p, "https": p})
            # print(response.json())
        except:
            # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
            # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
            tempList.remove(p)
            # print("Skipping. Connnection error")
    print("#####    Clean process finished. %d proxy is available to Use.   #####" % len(tempList))
    return tempList


if __name__ == '__main__':
    get_list()

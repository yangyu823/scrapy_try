import json
import requests
from tqdm import tqdm
from itertools import cycle
from lxml.html import fromstring

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

txt = requests.get("https://proxy.rudnkh.me/txt").text
tempList = (txt.split('\n')[:-1])

with open('list_initial.json') as origin:
    initial = json.load(origin)
    origin.close()


def test():
    if tempList[0] not in initial:
        with open('list_initial.json', 'w') as infile:
            json.dump(tempList, infile, indent=4, ensure_ascii=False)
            infile.close()
            print("###########    Update Source Proxy List")
        testUrl = 'https://httpbin.org/ip'

        for p in tqdm(tempList, desc='Clean Proxy List ...'):
            # print("Request #%s" % p)
            try:
                response = requests.get(testUrl, timeout=2, proxies={"http": p, "https": p})
                # print(response.json())
            except:
                # Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work.
                # We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url
                tempList.remove(p)
                # print("Skipping. Connnection error")
        print("###########    Updated Usable Proxy List. %d proxy is available to Use." % len(tempList))

        with open('list_final.json', 'w') as outfile:
            json.dump(tempList, outfile, indent=4, ensure_ascii=False)
            outfile.close()
    else:
        print("###########    Proxy list already up to date")
        return


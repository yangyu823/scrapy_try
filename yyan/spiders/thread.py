#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
from time import time as timer
from urllib.request import urlopen

urls = ["http://www.google.com", "http://www.apple.com", "http://www.baidu.com", "http://www.amazon.com",
        "http://www.facebook.com", "http://www.qq.com", "http://www.taobao.com", "http://www.jd.com",
        "http://www.xunlei.com", "http://www.360.com", ]


def fetch_url(url):
    try:
        response = urlopen(url)
        return url, response.read(), None
    except Exception as e:
        return url, None, e


start = timer()
# Threading value |||| Below ||||
results = ThreadPool(11).imap_unordered(fetch_url, urls)
for url, html, error in results:
    if error is None:
        print("%r fetched in %ss" % (url, timer() - start))
    else:
        print("error fetching %r: %s" % (url, error))
print("Elapsed Time: %s" % (timer() - start,))

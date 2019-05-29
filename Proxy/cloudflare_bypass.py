#!/usr/bin/python

from selenium import webdriver
from time import sleep
import http
import requests

print('Launching Firefox..')
browser = webdriver.Firefox()
print('Entering to skidpaste.org...')
browser.get("https://hidemyna.me/en/proxy-list/")
print('Waiting 10 seconds...')
sleep(10)
a = browser.get_cookies()
print('Got cloudflare cookies:\n')
print('Closing Firefox..')
browser.close()

h = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}

b = http.cookiejar.CookieJar()

for i in a:
    ck = http.cookiejar.Cookie(name=i['name'], value=i['value'], domain=i['domain'], path=i['path'], secure=i['secure'],
                               rest=False, version=0, port=None, port_specified=False, domain_specified=False,
                               domain_initial_dot=False, path_specified=True, expires=i['expiry'], discard=True,
                               comment=None, comment_url=None, rfc2109=False)
    b.set_cookie(ck)

r = requests.get('https://hidemyna.me/en/proxy-list/?maxtime=1000&type=s#list', cookies=b, headers=h)
print(len(r.content))
print(r.status_code)




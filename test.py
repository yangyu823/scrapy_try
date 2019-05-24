import json
import os
import urllib
import requests
from time import time as timer
from tqdm import tqdm
# from multiprocessing.pool import ThreadPool
from multiprocessing import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

with open("img.json", "r") as output:
    datastore = json.load(output)

    lst = list(datastore)


    # print(datastore[list(datastore)[0]])
    # print(lst)

    def getdown(key):
        try:
            value = datastore[key]
            coverPath = '%s/meizi/%s' % (os.getcwd(), key)
            urllib.request.urlretrieve(value, coverPath)
            # return ("The key and value are ({}) = ({})".format(key, value))
            # return key, None
        except Exception as e:
            return "Image file %r can not be downloaded. %s" % (key, e)



    # getdown(datastore)
    if __name__ == '__main__':
        with tqdm(total=len(lst)) as t:
            for _ in Pool(20).imap_unordered(getdown, lst):
                t.update(1)


    print("All done")

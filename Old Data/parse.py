import readline
#import datetime
from urlextract import URLExtract
import requests

extractor = URLExtract()

known_urls = []
req = []
url_status = []

f = 'all_lists.txt'

with open(f) as file:
    while (line := file.readline().rstrip()):
        items = line.split("\t")
        desp = items[2]
        print(desp)
        urls = extractor.find_urls(desp)
        res = [ele for ele in urls if ele != []]
        # print(res)
        # for url in urls:
        #     if url not in known_urls:
        #         if "http://" not in url:
        #             url = "https://" + url
        #             known_urls.append(url)

#print(known_urls[0:20])

# for i in known_urls:
#     # print(i)
#     try:
#         req = requests.get(i)
#         print(req.status_code)
#     except:
#         raise

# for i in req:
#     print(req[i])
    # r.status_code
    # if 
    # url_status

# all_lists = open(f, 'r')

# res = all_lists.readline()
# print(all_lists.readline())
# print(type(all_lists))

# for line in res:
#     items = line.split("\t")
#     desp = items[2]
#     urls = URLExtract.find_urls(desp)

    # for url in urls:
    #     if url not in known_urls:
    #         known_urls.append(url)
    #         try:
    #             r = requests.get(url)
    #         except requests.ConnectionError:
    #             print("Failed To Connect")


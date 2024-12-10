'''
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# 加入headers資訊來模擬瀏覽器的行為
url = "https://www.kingstone.com.tw"
headers_chrome = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
headers_safari = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15'}
#request = Request(url,headers = headers_chrome)
request = Request(url)

with urlopen(request) as page:
    html = page.read().decode('utf-8')
print(page.status)
'''

import requests

url = "https://www.kingstone.com.tw"
headers_chrome = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
headers_safari = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15'}

#resp = requests.get(url)
resp = requests.get(url, headers = headers_chrome)
#resp = requests.get(url, headers = headers_safari)
print(resp.status_code)
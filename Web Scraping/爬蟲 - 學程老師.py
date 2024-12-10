import requests
from bs4 import BeautifulSoup
url = 'https://steam.nycu.edu.tw/teachers/'
response = requests.get(url, verify = False)
response.encoding = 'UTF-8'
sp = BeautifulSoup(response.text, 'html.parser')
print(sp.title)
# datas = sp.find('div', class_ = 'result-game-root')
# title = datas.find('div', class_ = 'period-title')
import requests
from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com'
response = requests.get(url)
response.encoding = 'UTF-8'
sp = BeautifulSoup(response.text, 'html.parser')
print(sp.title)
# datas = sp.find('div', class_ = 'result-game-root')
# title = datas.find('div', class_ = 'period-title')
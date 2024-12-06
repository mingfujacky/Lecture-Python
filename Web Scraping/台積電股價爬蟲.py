from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://tw.stock.yahoo.com/quote/2330.TW'    # 台積電 Yahoo 股市網址
with urlopen(url) as page:    # 取得網頁內容
    html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')    

#找到h1的內容 (台積電)
company = soup.find_all('h1')[1].text

a = soup.select('.Fz\(32px\)')[0].text     # 找到第一個 class 為 Fz(32px) 的內容
b = soup.select('.Fz\(20px\)')[0].text     # 找到第一個 class 為 Fz(20px) 的內容

# 漲或跌的狀態
s = ''
c = soup.select('#main-0-QuoteHeader-Proxy')[0]
print(c.prettify())
d = c.select('.C\(\$c-trend-down\)')[0]['class'][-1]
if d == 'C($c-trend-down)':
    s = '-'
if d == 'C($c-trend-up)':
    s = '+'
print(f'{company} : {a} ( {s}{b} )')   # 印出結果

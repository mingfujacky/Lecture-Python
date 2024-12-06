from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://code-gym.github.io/spider_demo/'
with urlopen(url) as page:
    html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

#print(soup)
#print(soup.prettify())

# find data
print(soup.h1)
print(soup.h1.text)

# for h3 in soup.find_all('h3'):
#     #print(h3.prettify())
#     if h3.a is not None:
#         print(h3.a.prettify())
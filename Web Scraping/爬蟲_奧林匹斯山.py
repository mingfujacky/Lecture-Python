from pathlib import Path
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import webbrowser

url = 'http://olympus.realpython.org/profiles/dionysus'
with urlopen(url) as page:
    html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

#印出網頁內容
print(soup.get_text())
print(soup.prettify())

#將網頁輸出存檔到local
file_path = Path.cwd() / 'output1.html'
with file_path.open('w', encoding = 'utf-8') as file:
    file.write(str(soup))

#打開圖檔 & 儲存圖檔
images = soup.find_all('img')
for i in range(0, len(images)):
    image_url = 'http://olympus.realpython.org' + images[i]['src']
    webbrowser.open(image_url)
    image_path = Path.cwd() / images[i]['src'][8:]
    urlretrieve(image_url, image_path)
    
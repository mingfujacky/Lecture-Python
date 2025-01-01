---
marp: true
html: true
theme: default
paginate: true
---
# Web Scraping (網路爬蟲)
---
# 在學習網頁爬蟲之前 ...
[前端, 後端, 資料庫, 傻傻分不清](https://youtu.be/G-Ks1XYGyaY?si=N2HKBHyOD5fqVBvN
)

---
# HTTP Request / Response Model
- requests module: get / put URL
- bs4 module: parse HTML content
![bg right:60% w:600](https://www.researchgate.net/profile/Kereshmeh-Afsari/publication/311571526/figure/fig3/AS:438170157359106@1481479314691/HTTP-request-response-model.png)

---
# Response Content - HTML Tags based on DOM (文件物件模型)

<div style="text-align: left;">
  <iframe src="http://localhost:8000/Documents/交大教學/Python講義4/html/dom_illustration.html" width="30%" height="250px"></iframe>
</div>

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Text</title>
</head>
<body>
    <h1>My Header</h1>
    <p>My Paragraph</p>
</body>
</html>
```


![bg right:40% w:500 DOM](https://miro.medium.com/v2/resize:fit:1228/format:webp/1*WvPNmqXTSTijB_mSO8PMjA.png)

---
# Response Content - WebPage
- enable local host web server: python3 -m http.server 8000

<div style="text-align: left;">
  <iframe src="http://localhost:8000/Documents/交大教學/Python講義4/html/html_demo.html" width="50%" height="200px"></iframe>
</div>

```html
<!DOCTYPE html>
<html>
<head>
    <title>我是網頁標題</title>
</head>
<body>
    <h1 class="large">我是標題</h1>
    <div>
      <p>我是段落</p>
      <img src="https://www.nycu.edu.tw/userfiles/nycuch/images/20230915173911063.png" alt="我是圖片"><br>
      <a href="http://www.e-happy.com.tw">我是超連結</a>
    </div>
</body>
</html>
```

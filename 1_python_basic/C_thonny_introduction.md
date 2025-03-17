---
marp: true
theme: default
class: invert
size: 16:9
paginate: true
footer: 國立陽明交通大學 電子與光子學士學位學程
headingDivider: 1
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
  
  .middle-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 75%;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid img {
    width: 100%;
  }
  .red-text {
    color: red;
  }
  
  .blue-text {
    color: lightskyblue;  
  }

  .small-text {
    font-size: 0.90rem;
  }
---
# 地端 (本機) 環境 - Thonny
- 開發環境: Thonny, a Python IDE (Integrated Development Environment)
- 翻譯工具: Python3, provided by Thonny
- 運算資源: 使用本機的CPU和Memory

# 安裝 Thonny
- 瀏覽器中搜尋 ”thonny”，到 thonny.org 網站
- mouse-over ”Mac” or “Windows”
- 下載最新版本 v4.1.7, 依據作業系統不同進行安裝
- 點擊Thonny 圖示, 啟動Thonny
- 寫一行指令 print('hello world') 並執行
- 將檔案命名為 first_python_on_thonny.py, 並存檔
- 在檔案總管中找到這個檔案
- 關閉 Thonny
- 打開 Thonny, 功能列表 File - Open 找到 first_python_on_thonny.py,  並重新載入

# Thonny 簡單操作
- 快速存取工具列
- 功能視窗
- Python shell

# Code Editor vs Python Shell
- Editor
  - 程式寫作區, 編寫陳述/敘述 (Statement)
  - 若需輸出到螢幕, 需使用 print() 函式,輸出結果會在 Python shell 中出現
- Python Shell
  - 互動式的執行 statement 或是運算式 (Expression)
  - 無需使用 print() 函式就可以檢視變數內容

# Thonny 使用介紹
[Thonny – 初學者利器] (https://youtu.be/VLo1YM83XO8?si=2NKHxtgKnaXmA9J4)

# Lab: 使用Thonny印字串
1. 使用Thonny執行以下程式，並以 ’do_print.py’ 存檔 (只利用print指令)
```python
  *
 ***
*****
  |  
```



2. 關閉Thonny
3. 重新打開 do_print.py

# Lab: 使用 Thonny 做數學
使用Thonny執行以下程式，並以 ’do_math.py’ 存檔
```python
num1 = 1
num2 = 2
sum = num1 + num2
print(sum)
```

# W3 School
[Get Started] (https://www.w3schools.com/python/exercise.asp?x=xrcise_getstarted1)

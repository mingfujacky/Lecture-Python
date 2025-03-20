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

  .brown-text {
    color: brown;  
  }

  .small-text {
    font-size: 0.90rem;
  }
---

# Formosa OJ
- Python Class On-line Judge System – Formosa OJ
- https://formosa.oj.cs.nycu.edu.tw/signin/
- 半導體基地的學生請使用 Google OAuth2 登入
- 學士後專班的學生請使用 NYCU OAuth2 登入
- 選擇 "55 林志偉老師 Python 課程" 進入

# string.split()
- 用來將字串分割成列表的方法
- 根據指定的分隔符，將字串切割成多個子字串，並返回一個列表
```python
str.split(sep=None, maxsplit=-1)
# sep（optional）：指定分隔符, 預設為 None，這表示會自動以 空格、\t、\n 為分隔符
# maxsplit (optional):指定分割次數, 預設為-1，表示不限制分割次數（將分割所有可能的部分）
# 返回一個list，包含分割後的子字串
```

# Example of string.split()
```python
text = "Python is great"
result = text.split()  # 預設以空白字元分割
print(result)  # 輸出 ['Python', 'is', 'great']
```
```python
text = "apple,banana,orange"
result = text.split(",")  # 指定逗號作為分隔符
print(result)  # 輸出 ['apple', 'banana', 'orange']
```
```python
text = "apple-banana-orange"
result = text.split("-", maxsplit=1)  # 最多分割一次
print(result)  # 輸出 ['apple', 'banana-orange']
```

# Read Exercise Input

<span class="brown-text">**DO NOT NEED PROMOTE MESSAGE IN INPUT()!!**</span>

|Case                       |Input         |Get input       | Example
|---------------------------|--------------|----------------|-------------------
|one line string            |"John"        |my_str = input()| OJ#1868 
|one line number            |"100"         |n = int(input()) | OJ#1840
|one line two numbers       |"10 20"       |a, b = list(map(int, input().split())  | OJ#1841
|one line not fixed number  |"1 2 3 4 5 6" |x = list(map(int, input().split())) |

# Part 1
<style scoped>
table {
  font-size: 20px;
}
</style>
|PID|Problem|Lab
|---|-------|--------
|1840|整數的平方|1G
|1841|整數相加|1G
|1842|圓周長及圓面積|1J
|1845|字串組曲|2A
|1846|菜鳥的年資|1H
|1847|你在說迴文嗎？|2B
|1848|數字位數加總|2B
|1849|Merry X'mas|1I
|1854|簡易字串運算|2A
|1855|匯率轉換|

# Part 2
<style scoped>
table {
  font-size: 20px;
}
</style>
|PID|Problem|Lab
|---|-------|--------
|1856|簡易型開票統計|
|1857|最遠的距離|
|1858|多層金剛鑽|
|1868|Say Hello|1G
|1869|變數交換|2C
|1875|串列元素改位子|
|1876|移除重複元素並排序|
|1877|找出水仙花數|
|1878|生日快樂|
|1879|分數判斷|1H

# Part 3
<style scoped>
table {
  font-size: 20px;
}
</style>

|PID|Problem|Lab
|---|-------|--------
|1880|找質數|1I
|1881|n 階乘|
|1882|判斷等比數列|
|1883|信用卡號驗證|
|1884|生命靈數|
|1885|四則運算|
|1886|完全平方和|
|1895|月月是好月|
|1933|早安 Python|1G
|1974|凱撒密碼|

# Part 4
<style scoped>
table {
  font-size: 20px;
}
</style>
|PID|Problem|Lab
|---|-------|--------
|1975|最小公倍數(LCM)|
|1976|Tic-Tac-Toe 判斷勝負|
|1977|幾A幾B|
|1978|停車收費|
|1979|找因數|
|1980|出國換錢|
|1981|派派村水桶題|
|1982|直角三角形|
|1983|Two Sum|
|1986|左左右右|

# Lab:
1. write OJ#1933  (早安 Python, no input)
2. write OJ#1868  (Say Hello, input a string)
3. write OJ#1840  (整數的平方, input a number)
4. write OJ#1841  (整數相加, input two numbers)
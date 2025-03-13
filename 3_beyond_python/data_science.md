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
    color: blue;  
  }

  .small-text {
    font-size: 0.80rem;
  }
---
# 資料科學超微板

# 資料工作者
![bg right:65% w:700 Data Jobs](https://media.licdn.com/dms/image/v2/D5612AQHA6TVXNrLLyQ/article-inline_image-shrink_400_744/article-inline_image-shrink_400_744/0/1693358152818?e=2147483647&v=beta&t=X9Ve46WqlmZjnJ70Y6sU20COgXjTlgSZc-fe5WFT088)

# 資料層級
![bg right:65% w:500 Data Hierarchy](https://ecampusontario.pressbooks.pub/app/uploads/sites/2109/2021/11/data_hierarchy-1.png)

# 資料量單位
![bg right:65% w:500 Data Units](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyJ3RkSNsT0CivAMv4HzQIi7cEAoO8PaUyEw&s)

# 字元編碼：ASCII
ASCII: American Standard Code for Information Interchange
一個字元使用一個byte, 總共定義128個字元
- 英文大小寫字母
- 阿拉伯數字
- 標點符號、括號以及其它符號
- 控制字元，如響鈴，退格，換行，換頁，跳出資料通訊，退出鍵 
![bg right:50% w:500 ASCII](https://www.runoob.com/wp-content/uploads/2022/03/ascii-1-1.png)

# 字元編碼：Unicode
Unicode用兩個byte來表示一個字元, 給每個字元定義一個唯一的編碼, 同一個字元, 不論是什麼平臺、不論是什麼程式語言都一樣的編碼。
字元 |Unicode   
------|:----
H|00000000 01001000
i|00000000 01101001
!|00000000 00100001
你|01001111 01100000
好|01011001 01111101

# 字元編碼：UTF-8
- 8-bit Unicode Transformation Format
- 為了節省空間，UTF-8優化Unicode的編碼, 用一至四個bytes對Unicode字元集的所有字元進行再編碼

<style scoped>
table {
  font-size: 20px;
}
</style>

字元 |UTF-8   
------|:----
H|01001000
i|01101001
!|00100001
你|11100100 10111101 10100000
好|11100101 10100101 10111101

# 數字編碼：二進位
![bg right:50% w:500 數字編碼](https://kopu.chat/wp-content/uploads/2017/04/e89ea2e5b995e5bfabe785a7-2017-04-28-21-26-01.png)

# 數字編碼：二/ 八 / 十六 進位 
![bg right:40% w:500 數字編碼](https://docs.f5ezcode.in/~gitbook/image?url=https%3A%2F%2F3362868160-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-L_r09305cCOiVsKX4GC%252F-LdbAaNUSjLJ4JCj636w%252F-LdbBns5IfBitI948lJe%252F2.1.5.png%3Falt%3Dmedia%26token%3D292a4823-95ed-4d54-ac2b-a1aa32c01852&width=768&dpr=4&quality=100&sign=9d87100d&sv=1)

- 十進位：0 ~ 9 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  **45<sub>10</sub>**
- 二進位(bin)：0, 1  &nbsp;&nbsp;  **101101<sub>2</sub>**
- 八進位(oct)：0 ~ 7 &nbsp;&nbsp;  **55<sub>8</sub>**
- 十六進位(hex)：0 ~ 9, A ~ F &nbsp;&nbsp;  **2d<sub>16</sub>**
*-* A: 10
*-* B: 11
*-* C: 12
*-* D: 13
*-* E: 14
*-* F: 15

# 數字編碼：計算十進位轉二進位
![bg right:60% w:700 數字編碼轉換](
https://docs.f5ezcode.in/~gitbook/image?url=https%3A%2F%2F3362868160-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-L_r09305cCOiVsKX4GC%252F-LdbAaNUSjLJ4JCj636w%252F-LdbBjSEjvD4kSdxDMv5%252F2.1.4.png%3Falt%3Dmedia%26token%3D47bd4afd-37cf-42f9-b0b8-da0c9f4ab929&width=768&dpr=2&quality=100&sign=56845e24&sv=1)

# Lab: 編碼轉換
- 將十進位的20轉換為二進位, 八進位及十六進位
- 11110<sub>2</sub>，1E<sub>16</sub>， 36<sub>8</sub>, 以十進位制而言, 分別是多少
- 1.2GB 相當於多少 MB, 又相當於多少KB 
- 在ASCII 表格中, 'M' 和 'm’ 誰的數值大
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
# Python的起源
- [吉多·范羅蘇姆 Guido van Rossum](https://youtu.be/Wd-QMD-c7so?si=WfEnD_2srWDLwger)，荷蘭人，為Python的最初設計者
  - Python 誕生於1990年代
  - 以BBC電台的 “Monty Python’s Flying Circus” 命名

- 吉多對 Python 的目標
  - 一門簡單直觀的語言並與競爭者一樣強大
  - 開源，以便任何人都可以為它做貢獻
  - 代碼像純英語那樣容易理解
  - 適用於短期開發的日常任務

# Python 過去現在與未來
- Python 重要版本演進：v1.0 (1994), v2.0 (2000), v3.0 (2008), v4.0 (maybe no)
- Python 3 有一些特性和之前 Python 2 是不相容的, 現在如果要學習Python,可直接學習Python 3, 但在接手維護既有程式時，要先確定版本
- Lastest Python version v3.13.5 (2025/06/11)
- Python 的應用領域
  - 科學計算與大數據分析
  - 人工智慧與機器學習
  - 系統維運腳本開發
  - 網站開發
  - 動畫遊戲開發，網路爬蟲、駭客攻防

# Python 的特點
- 容易學習：語法簡單直白，可讀性高
- 免費函數庫：Python內建及其第三方函數庫皆為開源軟體，免費
- 跨平台
- 應用層面廣
- 豐富的學習資源，社群及技術文件
![Python Feratures bg right:40% w:500](https://worlddotwales.wordpress.com/wp-content/uploads/2019/03/image.png)

# Python 的不足
- 執行速度較慢：Python 是解釋型語言，執行速度不如編譯型語言如 C/C++
- 記憶體消耗較大：Python 的記憶體管理較為寬鬆，可能導致較高的記憶體消耗
- 多線程性能：Python 的全域直譯器鎖（GIL）限制
- 不適合移動端開發：雖然有一些框架可以用於移動端開發，但 Python 在移動端的生態系統不如其他語言如 Java 或 Swift 成熟
- 動態類型：雖然這是 Python 的一個優點，但也可能導致在大型項目中出現類型錯誤，特別是在沒有良好測試的情況下  


# Online Resources
- [w3schools.com](https://www.w3schools.com/python/default.asp)
- [Realpython.com](https://realpython.com/)
- [Python 官網](https://python.org)
- [Python tutor](https://pythontutor.com/python-compiler.html#mode=edit)
- [STEAM 教育學習網](https://steam.oxxostudio.tw/category/python/index.html)
- [資料科學家的工作日常](https://www.youtube.com/@dsdaily)

# Reference Books
- [Real Python 人氣站長教你動手寫程式](https://www.books.com.tw/products/0010955256?-srsltid=AfmBOopOYkEedUxjBdVTffrrNdGFvMn-SX_aVAbDZFHiKravuV9VQ_U4)
- [少年Py的大冒險：成為Python數據分析達人的第一門課](https://www.books.com.tw/products/0010988928?sloc=main)
- [Python 技術者們：練功！](https://www.books.com.tw/products/0010834816?sloc=main)

# Coding-style IDE vs. Notebook-style IDE
- Coding-style IDE: Thonny, 使用 .py 為副檔名
- Ｎotebook-style IDE: CoLab 使用 .ipynb 為副檔名

# Python for 初學者
![Newbie Programmer bg right:30% w:350](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjb_CZf_pQ9Zkg3ExzYj-WrOL8XFsCV8U7Dh0r5wDPWJrUdVGdhwNWZvx6_Mh2vh9Kxd1iyAV5jbcbXh67McVHuCl-FBe8-tv30ZYXBrksuKi6_dlwbjhUzfTVmEk6RmwsEjq_hJiBv1K4/s1600/S__5816325.jpg)

<span class="small-text">
初聽說 Python 簡單又強大，於是心懷期待，急於求成地妄想著自己可以一步登天，但現實是什麼呢？當你面對新問題時，沒有程式設計思路，甚至連問 AI 的問題都不知道該怎麼問<br>
第一步：Python 的本質是解決問題的工具： 程式設計的核心是「輸入、處理、輸出」，你需要掌握這種基本框架，才能靈活運用。<br>
第二步：物件導向編程（OOP）： 這是程式管理和組織的基礎，讓你寫出的程式是有結構、有邏輯，能隨需求變化進行擴展。 <br>
第三步：資料結構與演算法：解決問題時，好的資料結構和高效的演算法會讓你的程式設計如虎添翼。<br>
最後才是 AI/ML 等高階技能：有了基礎的邏輯思維和結構設計能力，學習這些技術才會事半功倍。
</span>
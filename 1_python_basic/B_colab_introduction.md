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
# 安裝 Google Colab

# 執行 Python 的環境

- <span class="blue-text">開發環境</span>：編輯 source code
  - 文字編輯器: Notepad
  - IDE (整合開發環境): Thonny, VS Code
- <span class="blue-text">翻譯工具</span>：翻譯 source code 成為 machine code
  - 直譯器 Interpreter
- <span class="blue-text">運算資源</span>：執行 machine code
  - 雲端
  - 本機

![bg right 40% w:90% Python Interpreter](https://www.datasciencecentral.com/wp-content/uploads/2021/10/8784089862.jpeg)

# 雲端環境 - Colab
- 開發環境: Google Colaboratory
- 翻譯工具: Python3 interpreter, provided by Google Colab
- 運算資源: 使用Google cloud 的CPU和Memory

<p class="small-text">
- 使用自己的Google帳號登入，進入”雲端硬碟”<br>
- 點選左上方新增按鈕新增文件，選擇”Google Colaboratory”，新增一個Colab Notebook<br>
- 若無”Google Colaboratory”的選項，點選 ”+連接更多應用程式”，找到Google Colaboratory後安裝<br>
- 重新命名檔名為FlyPython.ipynb (副檔名 ipynb 代表 interactive python notebook)<br>
- 輸入簡單指令來確認CoLab安裝完成：CTRL-ENTER, SHIFT-ENTER 或 PLAY按鈕執行指令<br>
- 儲存第一隻Python程式：File/Save, or CTRL+S<br>
- 回 Google Drive, 檢查程式是否存在雲端硬碟內 
</p>

# Colab 簡單操作
- Rename file
- Save file (CTRL + S)
- Run cell (CTRL + ENTER, SHIFT + ENTER)
- Delete / add / move cells
- Add markdown text
- Mount (掛載) Google 雲端硬碟
- 跟Python環境相關的指令
  - !python --version
  - !pip list

# Colab 使用介紹
[影片 開始使用 Google Colab](https://youtu.be/eJCXFIoOwdw?si=_HyCFGAgGT4HAYlx)

# Lab: 使用Colab來寫程式
- 把CoLab 當計算機計算
   - 鍵入 2 * 4 * 6 然後執行
   - 鍵入 20 + 4 * (3+2) 然後執行
- 鍵入 print (‘Hello Python, I need you!!’) 然後執行
- 存檔成 first_python_on_colab.ipynb
- 關閉 CoLab, 在Google雲端硬碟上找到 first_python_on_colab.ipynb, 並且打開它
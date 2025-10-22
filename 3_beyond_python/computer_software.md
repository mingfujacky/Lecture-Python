---
marp: true
theme: default
class: 
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
    font-size: 0.80rem;
  }
---
# 電腦軟體超微板

# 電腦的軟體
<span class="blue-text">作業系統 (Operating System, OS) </span>
- 讓使用者能更方便的操作電腦
  - 管理檔案系統 & 使用應用程式
  - 操作網路 & 控制多媒體裝置
- 使電腦資源得以更有效率的運用
  - 管理處理器和記憶體
  - 控制輸入與輸出裝置
- 提供程式執行的環境

<span class="blue-text">應用程式 (Applications, App)</span>
Chrome, Anti-virus, Office, Game

![bg right:50% w:500 Software](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEic7E9gu3x3rcWjb_7hpj7pjc0ZXNFg-nyOXLdB7PfVhTeu_6V89k11HqRnnMPrC1Mt6n84CvxidZ1hyW-NF3pDWdAjCjAEmHg7cOb7BARw_HZRJYn0QEB2xd1opPXUq5i_J8ucnWJNk66j/s1600/0000.jpg)

# 以文字指令來操作作業系統
- 平時大多數使用者用圖形化界面(GUI, Graphic User Interface)來操作作業系統，求其直覺方便
- 系統管理員或資深資訊工程師會使用終端機來操作作業系統，求其效率及酷
- MAC: 終端機 (Terminal)
![Mac Terminal w:50](
https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Terminalicon2.png/240px-Terminalicon2.png)
- Windows: 命令提示列 (Prompt), 使用 Windows鍵 + R 或是搜尋 CMD
![Windows Prompt w:250](https://i0.wp.com/image.walker-a.com/2021/10/dbox/dbox-02.jpg?w=1200&ssl=1)


# 電腦工作原理
[影片：學程式設計前，懂一些作業系統原理及操作](https://youtu.be/26EaLKPiskc?si=uUY8GJwegzzZEA6g)

# Lab: 使用命令列
1. 打開命令提示列或是終端機
2. 列印當前使用者名稱 (whoami)
3. 看看硬碟內有哪些檔案 (dir or ls)
4. 看看有沒有安裝Python軟體 (python –V or python3 –V)
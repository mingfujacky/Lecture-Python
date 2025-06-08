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
    color: blue;  
  }

  .small-text {
    font-size: 0.80rem;
  }
---
# 🤖 什麼是 Vibe Coding (氛圍編程)?
> Vibe coding = coding with AI pair-programmers like Copilot or ChatGPT
+ 由 OpenAI 前研究總監 Andrej Karpathy 提出
+ 使用生成式 AI（如 Copilot、ChatGPT）以自然語言生成程式
+ 初學者能快速產出結果，減少挫折、提升學習樂趣

# 😵 AI 強勢崛起，新鮮人面臨的就業挑戰 (1/3)
https://www.cw.com.tw/article/5135668

---
## 就業市場現況：新鮮人正被 AI 取代
- 2024 年新鮮人招募人數比 2023 年減少 25%
- 因 AI 導入速度遠高於其他行業, <u>金融、電腦科學領域</u>最受衝擊 
---
## AI 技術導致白領職務快速被取代
- 初階白領職位（如行銷分析、研究助理）正被自動化取代
- Claude Opus 4：AI 可持續數小時撰寫高品質程式碼

---
## 企業導向「AI優先」策略
- 新創與大公司已開始實施 AI 優先原則  
- 軟體工程師 L5 以下職缺大幅減少

---
## 人才培養鏈的斷裂危機
- 「跟在專家旁邊學習」的職場學徒模式正在消失
- 新鮮人將難以養成專業與晉升經驗

---
## 未來社會轉變與風險
- 若初階人才不再被培養，未來社會可能出現：
  - 精英統治的自動化團隊結構
  - 社會階級固化，向上流動困難
- 學者擔憂：「這可能改變整個人類社會的結構與技能傳承方式」


# 👊 AI 是工具，真正的力量來自你！
https://dailypythonprojects.substack.com/p/will-ai-replace-programmers-lets

---
## 😵‍💫 AI 時代的焦慮，你是否也有？
當 ChatGPT、Copilot、Cursor 陸續出現，很多人開始擔心：

- AI 會不會取代我們？
- 我還需要學程式嗎？
- 現在學 Python 還來得及嗎？

👉 **這些問題，其實歷史上都曾出現過！**

---

## 🚂 歷史經驗怎麼說？

| 技術變革        | 當時的擔憂           | 實際發展                   |
|-----------------|----------------------|----------------------------|
| CAD (電腦輔助設計) | 工程師會被取代       | 工程師反而更有生產力       |
| 虛擬化技術       | 系統管理員不再需要   | 系統管理員的角色進化了     |

🔁 **結論：每次技術進步，都讓專業人員變得更重要，而不是被淘汰。**

---

## 📣關於 AI 的真相是……

- AI 無法獨立部署核心系統  
- 沒有人會讓 AI 沒有監督地修改正式環境  
- **企業需要的不是 AI 本身，而是能監督並使用 AI 的人**

✅ 所以我們該問的不是：「AI 會不會取代我？」  
✅ 而是：「**我能不能駕馭 AI，讓它成為我的助力？**」

---
## 🤹 那我們該怎麼做？

如果你正在學 Python 或提升程式能力，請記住：

✅ **繼續學習 Python、演算法、系統設計等核心技能**
✅ **同時學會使用 AI 工具來加速開發流程**
✅ **讓 AI 處理重複工作，你則專注創造力**

---
## ⚙️ 軟體開發包括了
  - Why: 發覺痛點 / 對談需求
  - What: 用戶故事 / 驗收標準
  - How: 架構設計 / 代碼審查  
  - **When: 原型開發 / 編寫程式**
  - Who: 個人賦能 / 團隊導入  
  - Where: 自動測試 / 規模部署

---
## 🎯 你的角色正在轉變！

你將不只是「寫程式的人」，而是：

- 💡 系統設計者  
- 🔍 問題解決者  
- 🧭 AI 能力的監督與整合者

🔧 **AI 是工具，但你才是真正的主導力量！**

# 🚀 Vibe Coding 練習
- `GitHub Copilot w/ VS Code` 輸入一個句子，然後計算該句子內的字數，還有最長的字是哪一個
- `ChatGPT w/ Thonny` 請用Python寫'判斷某年是否為閏年'的程式
- `Gemini w/ Google Colab` Write a Python program to remove the background from an image file I just uploaded in Google Colab.


# 🔗 延伸閱讀：
+ [`影片` Vibe Coding是什麼](https://youtu.be/8me0juJCpWM?si=3tcdojzGbhJKxFGo)
+ [`評論`AI強勢取代！今年畢業生有多慘？](https://www.cw.com.tw/article/5135668)
+ [`評論` Vibe Coding 操作技巧與技能轉變](https://ikala.ai/zh-tw/blog/ikala-ai-insight/vibe-coding-intro/)
+ [`評論` AI取代程式設計師?](https://dailypythonprojects.substack.com/p/will-ai-replace-programmers-lets) 
+ [`影片` 高鐵票小工具](https://youtu.be/wuo3Gp09fEs?si=8bNNxXflqnAuNm-f)

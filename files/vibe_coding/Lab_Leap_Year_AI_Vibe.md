# 🧪 Lab: 判斷閏年（Leap Year）結合 AI Vibe Coding

## 🎯 目標
- 練習 Python 的條件判斷 (`if/elif/else`)
- 學習如何與 AI 工具（如 ChatGPT）合作寫程式
- 培養閱讀、理解與修改程式的能力

---

## 📍 Step 1. 題目說明

請撰寫一段 Python 程式，判斷輸入的年份是否為閏年。

### 🔍 判斷規則
- 如果年份可以被 4 整除但不能被 100 整除，或是可以被 400 整除，則為閏年。
- 否則為平年。

---

## 📍 Step 2. 自己寫寫看

請手動撰寫程式碼，**不要使用 AI 協助**，例如：

```python
# 範例輸入
year = int(input("請輸入西元年份："))

# 請寫出你的邏輯
# if ...:
#     print("是閏年")
# else:
#     print("不是閏年")
```

---

## 📍 Step 3. 與 AI 合作：Vibe Coding 練習

請嘗試以下 prompt，讓 ChatGPT 幫你產生程式碼：

```
Write a Python program to check if a given year is a leap year.
```

或更進階一點：

```
Can you write a function `is_leap_year(year)` that returns True if the year is a leap year, otherwise False?
```

📌 請觀察 AI 的寫法與你手寫的有何不同？有學到什麼更簡潔的寫法嗎？

---

## 📍 Step 4. 參考解法（由 AI 提供）

```python
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 測試數值
for y in [2000, 1900, 2024, 2023]:
    print(f"{y} 是閏年嗎？", is_leap_year(y))
```

---

## 📍 Step 5. 回顧與反思

請思考以下問題並作答：

1. 你一開始寫出來的邏輯和 ChatGPT 提供的有什麼不同？
2. 你覺得 AI 在這題目上幫助你的是什麼？
3. 若再次寫類似題目，你會用什麼方式開始？

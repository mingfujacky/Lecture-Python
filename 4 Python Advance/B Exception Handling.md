---
marp: true
html: true
theme: default
paginate: true
---
# 除錯與例外處理
---
# 常見的錯誤 - Syntax Error (語法錯誤)
- if-esle, for, while, def 沒有加冒號
- 判斷式中將 == 寫成 =
- 字串前後引號不成對

```python
if 5 > 3
    print("5 > 3")    
if 5 = 3:
    print("5 = 3")
print("5 is bigger than 3"") 
```
---
# 常見的錯誤 - Exception (例外)
- 語法正確但程式的執行因報錯而被迫中止
- Name Error
- Type Error 
- Zero Division Error
- Index Error
- Identation Error

```python
a = age + 1
print('1' + 1); print(6 / 0); print('python'[9])

if 5 == 5:
print('5 = 5')

 if 5 == 5:
     print('5 = 5')

```
---
# 常見的錯誤 - Environment Error (環境錯誤)
- 程式的執行環境所引發的錯誤
- 記憶體不足
- 讀一個不存在的檔案
- 檔案權限不足

```python
with open("a.txt", "r", encoding = "utf-8") as f:
    print(f.read())
```
---
# 除錯工具 - print()
- 利用 print() 將有嫌疑或需觀察的變數印出
```python
# translate "hello" to "h_e_l_l_o"
def add_underline(word):
    new_word = ''
    for i in range(len(word)):
        new_word = word[i] + '_'
    return new_word
print(add_underline('hello'))
```
```python
# correct code
def add_underline(word):
    new_word = ''
    for i in range(len(word)):
        new_word = new_word + word[i] + '_'
    new_word = new_word[:-1]
    return new_word
print(add_underline('hello'))
```
---
# 除錯工具 - debugger
- 利用除錯器 (debugger) 除錯
- step_over
- step_in
- step_out
- resume
---
# Lab: 根據錯誤訊息給的線索，修正程式碼
```python
'hello'[-6]
'hello'.upper('h')
'hello'.replace('a')
'hello'.count(3)
'hello'.count(h)
'hello' * '2'
```
---
# Lab: debug程式碼，讓執行得到正確的結果 

```python
# power_integer (2, 3) = 2 ** 3 = 8
def power_integer(num, p):
    result = 1
    while (p >= 0):
        result = result * num
        p = p - 1
    return result

print(power_integer(2, 3))
```
---
# 例外處理 (Execeptional Handling)
- 程式執行時的安全帶
- 若無例外處理(安全帶)，則程式遇見錯誤時將直接終止
- try-except
- try-except-else
- try-except-finally
- try-except-else-finally

![bg right:50% w:600](https://realpython.com/cdn-cgi/image/width=1394,format=auto/https://files.realpython.com/media/try_except_else_finally.a7fac6c36c55.png)

---
# Try-except

```python
try:
    num = int(input("Number: "))
    result = 1024 / num
    print(f"{result=}")
    with open('a.txt',"w") as f:
        f.write(result)
except ValueError as e:
    print("不能把字串轉換為整數!")
    print("錯誤訊息 --> ", e)
except ZeroDivisionError:
    print("不能除以0")
except:
    print('Ran into trouble. Please contact help desk!')    
```

---
# Try-except-else-finally
```python
try:
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    result = num1 // num2
except ValueError:
    print('Do NOT input non-number.')
except ZeroDivisionError:
    print('Second Number can NOT be zero.')
except:
    print('We got a trouble')
else:
    print(f"{num1} // {num2} = {result}")
finally:
    print("\ncode end!!")
```    
---
# Lab: 練習 try-except
請寫一段例外處理的程式，來避免程式當掉
```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict['address'])
```
<hr>

```python
try:
    my_dict = {'name': 'John', 'age': 30};
    print(my_dict['address'])

except KeyError as e:
    print(f"key: {e} is not in my_dict")
```    



'''
九九乘法表
寫一個python程式, 輸入一個句子，然後計算該句子內的字數，還有最長的字是哪一個
'''
sentence = input("請輸入一個句子: ")
words = sentence.split()
word_count = len(words)
longest_word = max(words, key=len)

print(f"字數: {word_count}")
print(f"最長的字: {longest_word}")

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
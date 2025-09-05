# 寫一個python程式, 輸入一個句子，然後計算該句子內的字數，還有最長的字是哪一個

def analyze_sentence(sentence):
    words = sentence.split()
    word_count = len(words)
    longest_word = max(words, key=len) if words else ""
    return word_count, longest_word

input_sentence = input("請輸入一個句子: ")
count, longest = analyze_sentence(input_sentence)
print(f"字數: {count}")
print(f"最長的字: {longest}")

if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
            print(f"{i} + {j} = {i + j}")
            print(f"{i} - {j} = {i - j}")
            print(f"{i} / {j} = {i / j if j != 0 else 'undefined'}")
            print(f"{i} // {j} = {i // j if j != 0 else 'undefined'}")
            
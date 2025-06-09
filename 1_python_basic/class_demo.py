"""
輸入一個句子，然後計算該句子內的字數，還有最長的字是哪一個
"""
def count_words_and_longest(sentence):
    words = sentence.split()
    word_count = len(words)
    longest_word = max(words, key=len) if words else ""
    return word_count, longest_word

if __name__ == "__main__":
    sentence = input("請輸入一個句子: ")
    word_count, longest_word = count_words_and_longest(sentence)
    print(f"字數: {word_count}, 最長的字: {longest_word}")
# Example usage:
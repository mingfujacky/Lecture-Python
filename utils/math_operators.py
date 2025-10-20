'''
math_operators.py 提供數學的四則運算函數
parameters : 兩個整數
return: 計算後結果
'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# test case
if __name__ == '__main__':
    print(add(1, 2))
    print(sub(1, 2))
    print(mul(1, 2))
    print(div(1, 2))

class Stack:
    ''' This is a Stack class to practice OOP.
        Created by Jacky Lin @ 2024/03/01
        Version: 1.0
    '''
    def __init__(self):
        self.stack = []
    
    # 複製List內容並回傳    
    def get_stack_elements(self):
        return self.stack.copy()
    
    # 把item參數指向的物件加到List尾端
    def add_one(self, item):
        self.stack.append(item)
        
    # 把item參數指向的物件加到List尾端, 重複n次
    def add_many(self, item, n):
        for i in range(n):
            self.stack.append(item)
            
    # 從list尾端移除物件
    def remove_one(self):
        self.stack.pop()
        
    # 從list尾端移除物件, 重複n次
    def remove_many(self, n):
        for i in range(n):
            self.stack.pop()
    
    # List 內有多少物件
    def size(self):
        return len(self.stack)
    
    # 從尾端開始列印List內所有的物件
    def prettyprint(self):
        for thing in self.stack[::-1]:
            print('|_', thing, '_|')
    
# main program
pancakes = Stack()
pancakes.add_one('blueberry')
pancakes.add_many('chocolate', 4)
print(pancakes.size())
pancakes.remove_one()
print(pancakes.size())
pancakes.prettyprint()
    
# construct Circle class
class Circle: #第一個字大寫, 最後要有冒號
    
    def __init__(self):  #未來當一個object被初始化時執行屬性的賦值
        self.radius = 0  #self 代表未來新建立的物件
        
    def change_radius(self, radius):  #寫method就跟寫function一樣
        self.radius = radius
    
    def get_radius(self):
        return self.radius
   
# construct Stack class   
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
circles = Stack()
one_circle = Circle()
one_circle.change_radius(2)
circles.add_one(one_circle)
for i in range(5):
    one_circle = Circle()
    one_circle.change_radius(1)
    circles.add_one(one_circle)
print(circles.size())
circles.prettyprint()
    
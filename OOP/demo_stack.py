class Stack:
    '''
    stack is FILO
    '''
    def __init__(self):
        self.stack_list = []
        
    def get_stack_elements(self):
        return self.stack_list.copy()
    
    def add_one(self, item):
        self.stack_list.append(item)
        
    def add_many(self, item, n):
        for i in range(n):
            self.stack_list.append(item)
    
    def remove_one(self):
        self.stack_list.pop()
    
    def remove_many(self, n):
        for i in range(n):
            self.stack_list.pop()
    
    def size(self):
        return len(self.stack_list)
    
    def prettyprint(self):
        for thing in self.stack_list[::-1]:
            print('|_', thing, '_|')
            


# # main program
# pancakes = Stack()
# pancakes.add_one('blueberry')
# pancakes.add_many('chocolate', 4)
# pancakes.prettyprint()
# print(pancakes.size())
# pancakes.remove_one()
# print(pancakes.size())
# pancakes.prettyprint()
# pancakes.remove_many(2)
# print(pancakes.size())
# pancakes.prettyprint()
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

# Evaluation of Postfix
def postfix(s):
    stack = Stack()

    for c in s:
        if c.isdigit():
            stack.push(int(c))
        elif c == '+':
            a = stack.pop()
            b = stack.pop()
            stack.push(a + b)
        elif c == '-':
            a = stack.pop()
            b = stack.pop()
            stack.push(b -a)
        elif c == '*':
            a = stack.pop()
            b = stack.pop()
            stack.push(a * b)
        elif c == '/':
            a = stack.pop()
            b = stack.pop()
            stack.push(b / a)

    print(stack.pop())
            

postfix("123*+")
postfix("456*+")
postfix("2 3 1 * + 9 -")
postfix("10 2 8 * + 3 -")

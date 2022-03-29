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

# Write a function in python that can reverse a string using stack data structure. Use Stack class
# from the tutorial.reverse_string("We will conquere COVID-19") should return 
# "91-DIVOC ereuqnoc lliw eW"
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    rstr = ''
    while stack.size() != 0:
        rstr += stack.pop()
    
    return rstr


# Write a function in python that checks if paranthesis in the string are balanced or not. 
# Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
def is_match(ch1, ch2):
    dt = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }

    return dt[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for char in s:
        if char == '{' or char == '[' or char == '(':
            stack.push(char)
        if char == '}' or char == ']' or char == ')':
            if stack.size() == 0:
                return False
            if not is_match(char, stack.pop()):
                return False

    return stack.size() == 0
 

# is_balanced("({a+b})")
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
s = Stack()
print(reverse_string("We will conquere COVID-19"))
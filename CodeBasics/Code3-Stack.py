from collections import deque

# # Using a list as a stack
# stack = []
# stack.append('https://www.cnn.com/china')
# stack.append('https://www.cnn.com/home')
# stack.append('https://www.cnn.com/world')
# stack.append('https://www.cnn.com/india')

# print(stack[-1])
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# # The issue with using a list as a stack is that list uses dymanic array internally and when it 
# # reaches its capacity it will reallocate a big chunk of memory somewhere else in memory area 
# # and copy all the elements. For example in below diagram if a list has a capacity of 10 and 
# # we try to insert 11th element, it will not allocate new memory in a different memory region, 
# # copy all 10 elements and then insert the 11th element. So overhead here is (1) allocate new 
# # memory plus (2) copy all existing elements in new memory area


# # Using deque as a stack
# stack = deque()
# # print(dir(stack))

# stack.append("https://www.cnn.com/")
# stack.append("https://www.cnn.com/india")
# stack.append("https://www.cnn.com/china")
# stack.append("https://www.cnn.com/world")
# print(stack)
# print(stack.pop())
# print(stack.pop())
# print(stack)


# Implement Stack class using a deque
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

s = Stack()
s.push(5)
s.push(9)
s.push(34)
s.push(78)
s.push(12)

print(s.container)
print(s.peek())
print(s.is_empty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())
print(s.pop())


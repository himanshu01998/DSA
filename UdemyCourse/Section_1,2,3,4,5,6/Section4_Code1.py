# Write a function called power which accepts a base and an exponent. The function 
# should return the power of the base to the exponent. This function should mimic 
# the functionality of math.pow() - do not worry about negative bases and exponents.
print("--------Power Solution--------")

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)

print(power(2, 4))


# Write a function factorial which accepts a number and returns the factorial of that number. 
# A factorial is the product of an integer and all the integers below it; e.g., factorial 
# four ( 4! ) is equal to 24, because 4 * 3 * 2 * 1 equals 24. 
print("\n--------Factorial Solution--------")

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

print(factorial(4))


# Write a function called productOfArray which takes in an array of numbers and returns 
# the product of them all.
print("\n--------Product Of Array Solution--------")

def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])
    
print(productOfArray([1,2,3,4,6]))


# Write a function called recursiveRange which accepts a number and adds up all the 
# numbers from 0 to the number passed to the function.
print("\n--------Recursive Range Solution--------")

def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)

print(recursiveRange(5))


# Write a recursive function called fib which accepts a number and returns the nth number in 
# the Fibonacci sequence. Recall that the Fibonacci sequence is the sequence of whole 
# numbers 0,1, 1, 2, 3, 5, 8, ... which starts with 0 and 1, and where every number thereafter 
# is equal to the sum of the previous two numbers.
print("\n--------Fibonacci Solution--------")

def fib(num):
    if (num < 2):
        return num
    return fib(num - 1) + fib(num - 2)

print(fib(6))

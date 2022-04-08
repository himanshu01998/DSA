# 1. Write a Python program to calculate the sum of a list of numbers.
def sum_of_list(elements):
    if len(elements) == 1:
        return elements[0]
    return elements[0] + sum_of_list(elements[1:])

elements = [2, 1, 5, 7, 2]
print("1st Exercise")
print(sum_of_list(elements))


# 2. Write a Python program to converting an Integer to a string in any base.
def to_string(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    return to_string(n//base, base) + convert_string[n % base]

print("\n2nd Exercise")
print(to_string(2835, 16))


# 3. Write a Python program of recursion list sum.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
def list_sum(elements):
    total = 0
    for element in elements:
        if type(element) == type([]):
            print(element)
            total = total + list_sum(element)
        else:
            total = total + element

    return total

elements = [1, 2, [3,4], [5,6]]
print("\n3rd Exercise")
print(list_sum(elements))


# 4. Write a Python program to get the factorial of a non-negative integer.
def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

print("\n4th Exercise")
print(factorial(5))


# 5. Write a Python program to solve the Fibonacci sequence using recursion.
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n5th Exercise")
print(fibonacci(7))

# 6. Write a Python program to get the sum of a non-negative integer.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(int(n / 10))

print("\n6th Exercise")
print(sum_digits(345))
print(sum_digits(45))


# 7. Write a Python program to calculate the sum of the positive integers 
# of n+(n-2)+(n-4)... (until n-x =< 0).
# Test Data:
# sum_series(6) -> 12
# sum_series(10) -> 30
def sum_until(n):
    if n == 0:
        return 0
    return n + sum_until(n-2)

print("\n7th Exercise")
print(sum_until(6))
print(sum_until(10))


# 8. Write a Python program to calculate the harmonic sum of n-1.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# 1 + 1/2 + 1/3 + 1/4 + 1/5 ....
def harmonic_sum(n):
    if n == 1:
        return 1
    return (1/n) + harmonic_sum(n-1)

print("\n8th Exercise")
print(harmonic_sum(7))
print(harmonic_sum(5))


# 9. Write a Python program to calculate the geometric sum of n-1. Go to the editor
# Note: In mathematics, a geometric series is a series with a constant ratio 
#       between successive terms.
# Example:
# 1 + 1/2 + 1/3 + 1/4 + 1/5 ....
def geometric_series(n):
    if n < 0:
        return 0
    return  1 / pow(2, n) + geometric_series(n-1)

print("\n9th Exercise")
print(geometric_series(7))
print(geometric_series(4))


# 10. Write a Python program to calculate the value of 'a' to the power 'b'.
# Test Data :
# (power(3,4) -> 81
def power(num, pow):
    if pow < 1:
        return 1
    return num * power(num, pow-1)

print("\n10th Exercise")
print(power(3, 4))


# 11. Write a Python program to find  the greatest common divisor (gcd) of two integers.
def gcd(num1, num2):
    low = min(num1, num2)
    high = max(num1, num2)
    
    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return gcd(low, high%low)

print("\n11th Exercise")
print(gcd(12, 14))
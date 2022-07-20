# Question 1 - Sum of digits 
# Eg. 12: 1+2 = 3, 35: 3+5 = 8

def sumofDigits(n):
    assert n>=0 and int(n) == n , 'The number has to be a postive integer only!'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(11111))


# Question 2 - Power of number
# Eg. base^power, 2^4: 2*2*2*2 = 16, 3^2: 3*3 = 9

def power(base,exp):
    if exp == 0:
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))

print(power(4, 2))


# Question 3 - Greatest common divisor of 2 numbers
# Eg.  8: 2*2*2  | GCD of 8,12 is
#     12: 2*2*3  | 2*2 = 4

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(gcd(12, 8))


# Question 4 - Convert decimal number to binary
# Eg. 10 -> 1010, 13 -> 1101

def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10*decimalToBinary(int(n/2))

print(decimalToBinary(1))

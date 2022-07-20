# Write a recursive function called reverse which accepts a string and returns a new 
# string in reverse.
print("--------Reverse String Solution--------")

def reverse(strng):
    if len(strng) <= 1:
      return strng
    return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])

print(reverse("python"))


# Write a recursive function called isPalindrome which returns true if the string passed 
# to it is a palindrome (reads the same forward and backward). Otherwise it returns false. 
print("\n--------Is Palindrome Solution--------")

def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])

print(isPalindrome("tacocat"))


# Write a recursive function called someRecursive which accepts an array and a callback. 
# The function returns true if a single value in the array returns true when passed to 
# the callback. Otherwise it returns false.
print("\n--------Some Recursive Solution--------")

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True
 
def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

print(someRecursive([1,2,3,4], isOdd))
print(someRecursive([4,6,8], isOdd))


# Write a recursive function called flatten which accepts an array of arrays and returns 
# a new array with all values flattened. 
print("\n--------Flatten Solution--------")

def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr 

print(flatten([1, [2, 3, [4], [[[5]]]]]))

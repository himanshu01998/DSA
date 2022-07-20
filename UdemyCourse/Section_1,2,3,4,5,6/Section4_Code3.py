# Write a recursive function called capitalizeFirst. Given an array of strings, 
# capitalize the first letter of each string in the array.
print("--------Capitalize First Solution--------")

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])

print(capitalizeFirst(['car', 'dog', 'bat', 'kite']))


# Write a recursive function called nestedEvenSum. Return the sum of all even numbers 
# in an object which may contain nested objects.
print("\n--------Nested Even Sum Solution--------")

def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]
    return sum

obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

print(nestedEvenSum(obj1))
print(nestedEvenSum(obj2))


# Write a recursive function called capitalizeWords. Given an array of words, 
# return a new array containing each word capitalized.
print("\n--------Capitalize Words Solution--------")

def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])

print(capitalizeFirst(['i', 'am', 'learning', 'recursion']))


# Write a recursive function called stringifyNumbers which takes in an object and 
# finds all of the values which are numbers and converts them to strings. 
# Recursion would be a great way to solve this!
print("\n--------Stringify Numbers Solution--------")

def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

print(stringifyNumbers(obj))


# Write a recursive function called collectStrings which accepts an object and 
# returns an array of all the values in the object that have a typeof string.
print("\n--------Collect Strings Solution--------")

def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

print(collectStrings(obj))

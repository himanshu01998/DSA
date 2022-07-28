# Write a function called middle that takes a list and returns a new list that contains all 
# but the first and last elements.
print("Exercise-1 Starts Here")

def middle(lst):
    new = lst[1:]  
    del new[-1]
    return new

myList = [1, 2, 3, 4]
print(middle(myList))


# Given 2D list calculate the sum of diagonal elements
print("\nExercise-2 Starts Here")

def sumDiagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]
    print("Sum of Diagonal:",sum)

myList2d = [[1,2,3], [4,5,6], [7,8,9]]
for item in myList2d:
    print(item)
sumDiagonal(myList2d)


# Given a list, write a function to get first, second best scores from the list
# List may contain duplicates
print("\nExercise-3 Starts Here")

def firstSecond(givenList):
    first = max(givenList)
    second = 0
    for item in givenList:
        if item > second and item < first:
            second = item
    print(first, second)

givenList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
firstSecond(givenList)


# Write a function to find the missing number in a given integer array of 1 to 100
print("\nExercise-4 Starts Here")

def missingNumber(myList, totalCount):
    listSum = sum(myList)
    sum1 = (totalCount * (totalCount + 1))/2
    print(int(sum1 - listSum))

missingNumber([1, 2, 3, 4, 6], 6)


# Write a function to find the duplicate number on given integer array/list
print("\nExercise-5 Starts Here")

def removeDuplicates(myList):
    newList = []
    for item in myList:
        if item not in newList:
            newList.append(item)
    return newList

print(removeDuplicates([1, 1, 2, 2, 3, 4, 5, 6, 5]))


# Write a function to find all pairs of an integer array whose sum is equal to a given number.
print("\nExercise-6 Starts Here")

def pairSum(myList, sum):
    newList = []
    for i in range(len(myList)-1):
        for j in range(i+1, len(myList)):
            if myList[i] + myList[j] == sum:
                newList.append(f"{myList[i]}+{myList[j]}")

    print(newList)

pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)

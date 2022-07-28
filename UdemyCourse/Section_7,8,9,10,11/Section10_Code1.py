import numpy as np

#  Question 1 - Find Missing Number
print("Q1 Starts Here")
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def findMissing(list, n):
    sum1 = sum(list)
    sum2 = 100*101/2
    print(sum2-sum1)

findMissing(mylist, 100)


# Question 2 - Sum of Pairs equals with given number
print("\nQ2 Starts Here")

def findPairs(list, sum):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (list[i]+list[j]) == sum:
                print(list[i],list[j])

findPairs(mylist, 100)


# Question 3 - Finding a number in array
print("\nQ3 Starts Here")
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)

findNumber(myArray, 12)


# Question 4 - Max Product of two int pairs of array
print("\nQ4 Starts Here")

def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j] > maxProduct:
                maxProduct = array[i]*array[j]
                pairs = str(array[i])+ "," + str(array[j])
    print(pairs)
    print(maxProduct)

findMaxProduct(myArray)


#Question 5 - Check each element of list if it is Unique or Duplicate
print("\nQ5 Starts Here")
def isUnique(list1):
    a=[]
    for i in list1:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(isUnique(mylist))


#Question 6 - Check if list 1 is Permutation of list 2
print("\nQ6 Starts Here")

def permuntation(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()

    if list1 == list2:   # if list1 == list2.reverse() -- false
        return True
    else:
        return False

print(permuntation([1,2,3], [3,2,1]))


# Question 7 - Rotate a matrix 90 degrees clockwise of NxN matrix
print("\nQ7 Starts Here")

def rotate_matrix(matrix):

    n = len(matrix)

    for layer in range(n // 2):
        print("Layer", layer)
        first, last = layer, n - layer - 1
        print("First", first, " Last", last)

        for i in range(first, last):
            # save top
            top = matrix[layer][i]

            # left -> top
            print(-i-1)
            print(matrix[layer][i], "=", matrix[-i - 1][layer])
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            print(matrix[-i - 1][layer], "=", matrix[-layer - 1][-i - 1])
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            print(matrix[-layer - 1][-i - 1], "=", matrix[i][- layer - 1])
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            print(matrix[i][- layer - 1], "=", top)
            matrix[i][- layer - 1] = top
            print()

    return matrix

# matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
matrix = np.array([[1,2,3,10], [4,5,6,11], [7,8,9,12], [13,14,15,16]])
print(matrix, "\n")

print(rotate_matrix(matrix))

################### PROBLEM 1 #######################
# When I try to find number 5 in below list using binary search, it doesn't work and 
# returns me -1 index. Why is that?
# numbers = [1,4,6,9,10,5,7]
# Answer: It is because the list is not sorted! Binary search requires that list has to be sorted.

################### PROBLEM 2 #######################
# Problem: Find index of all the occurances of a number from sorted list
# Solution here tries to find an index of a number using binary search. Now since the list is sorted,
# it can do left and right scan from the initial index to find all occurances of a given element
# This method is not most efficient and I want you to figure out even a better way of doing it. In
# any case below method is still effective

def binary_search(number_list, find_number):
    left_index = 0
    right_index = len(number_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_element = number_list[mid_index]

        if mid_element == find_number:
            return mid_index

        if mid_element < find_number:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def find_all_occurences(number_list, find_number):
    index = binary_search(number_list, find_number)
    indices = [index]

    # find indices on left hand side
    i = index - 1
    while i >= 0:
        if number_list[i] == find_number:
            indices.append(i)
        else:
            break
        i -= 1

    # find indices on left hand side
    i = index + 1
    while i < len(number_list):
        if number_list[i] == find_number:
            indices.append(i)
        else:
            break
        i += 1

    return sorted(indices)
    

if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    print(f"Single Binary Search for {number_to_find}:",binary_search(numbers, number_to_find))
    print(f"Find all Occurances for {number_to_find}:",find_all_occurences(numbers, number_to_find))


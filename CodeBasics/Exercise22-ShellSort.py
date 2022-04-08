# Sort the elements of a given list using shell sort, but with a slight modification. 
# Remove all the repeating occurances of elements while sorting.

# Traditionally, when comparing two elements in shell sort, we swap if first element 
# is bigger than second, and do nothing otherwise.

# In this modified shell sort with duplicate removal, we will swap if first element 
# is bigger than second, and do nothing if element is smaller, but if values are same, 
# we will delete one of the two elements we are comparing before starting the next pass 
# for the reduced gap.

# For example, given the unsorted list [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3], 
# after sorting using shell sort without duplicates, the sorted list would be:
# [0, 1, 2, 3, 5, 7, 8, 9]

def shell_sort(arr):
    size = len(arr)
    div = 2
    gap = size // div

    while gap > 0:
        index_to_delete = []
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= anchor:
                if arr[j-gap] == anchor:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor


        index_to_delete = list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[::-1]:
                del arr[i]
        div *= 2
        size = len(arr)
        gap = size // div

if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    shell_sort(elements)
    print(elements)
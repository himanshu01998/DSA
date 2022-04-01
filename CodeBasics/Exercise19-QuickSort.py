# Implement quick sort using lumoto partition scheme. This partition scheme is explained in 
# the video tutorial, you need to write python code to implement it. Check the pseudo code 
# here: https://en.wikipedia.org/wiki/Quicksort Check the section Lomuto partition scheme.

def swap(a, b, arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def quick_sort(elements, start, end):
    if len(elements) == 1:
        return

    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)


def partition(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)

    return p_index


if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [25, 22, 21, 10],
        [3, 7, 9, 11],
        [29, 15, 28],
        [],
        [6]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    for item in tests:
        quick_sort(item, 0, len(item)-1)
        print(item)
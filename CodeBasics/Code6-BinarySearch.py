import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def linear_search(number_list, find_number):
    for index, element in enumerate(number_list):
        if element == find_number:
            return index
    return -1

@timeit
def binary_search(number_list, find_number):
    left_index = 0
    right_index = len(number_list) - 1
    mid_index = 0

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

def binary_search_recursive(number_list, find_number, left_index, right_index):
    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(number_list) or mid_index < 0:
        return -1

    mid_element = number_list[mid_index]

    if mid_element == find_number:
        return mid_index

    if mid_element < find_number:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(number_list, find_number, left_index, right_index)

if __name__ == "__main__":
    numbers_list = [i for i in range(1, 1000)]
    
    print(linear_search(numbers_list, 999))
    print(binary_search(numbers_list, 999))
    print(binary_search_recursive(numbers_list, 999, 0, len(numbers_list)))
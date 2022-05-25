# Non-Divisible Subset - HackerRank (Problem Solving) 

from collections import defaultdict

def nonDivisibleSubset(k, s):
    # Write your code here
    mods = [item % k for item in s]

    freqs = defaultdict(int)
    for elem in mods:
        freqs[elem] += 1

    total = 0
    for key, val in freqs.items():
        if val == 0:
            continue

        if key == 0:
            total += 1
        elif (k - key) == key:
            total += 1
        elif key > (k - key):
            if (k - key) in freqs:
                total +=  max([val, freqs[k - key]])
            else:
                total += val
        elif key < (k - key):
            if (k - key not in freqs):
                total += val

    return total


s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
print(nonDivisibleSubset(7, s))
# s = [1, 7, 2, 4]
# print(nonDivisibleSubset(3, s))
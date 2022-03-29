# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this 
# file in python and print every word and its count as show below. Think about the best data 
# structure that you can use to solve this problem and figure out why you selected that specific 
# data structure.

dt = {}
with open('poem.txt', 'r') as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in dt:
                dt[word] += 1
            else:
                dt[word] = 1

print(dt)
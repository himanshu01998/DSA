# # Collision problem while inserting march 9 and may 2
# class HashTable:
#     def __init__(self):
#         self.MAX = 100
#         self.arr = [None for i in range(self.MAX)]

#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX

#     def __getitem__(self, index):
#         h = self.get_hash(index)
#         return self.arr[h]
    
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         self.arr[h] = val 

# t = HashTable()
# t['march 6'] = 390
# t['march 7'] = 150
# t['march 8'] = 190
# t['may 2'] = 30

# print(t.arr)
# print(t['march 8'])


# Hash Table Collision Handling Using Chaining
import enum


class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.Max

    def __getitem__(self, index):
        h = self.get_hash(index)
        for item in self.arr[h]:
            if item[0] == index:
                return item[1]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", self.arr[arr_index][index])
                del self.arr[arr_index][index]


t = HashTable()
t['march 6'] = 390
t['march 7'] = 150
t['march 8'] = 190
t['may 2'] = 30
print(t.arr)
t['march 6'] = 39
print(t['march 6'])
print(t['may 2'])

del t['may 2']

print(t['may 2'])
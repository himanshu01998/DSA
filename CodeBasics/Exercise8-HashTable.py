# Implement hash table where collisions are handled using linear probing. We learnt about linear 
# probing in the video tutorial. Take the hash table implementation that uses chaining and modify 
# methods to use linear probing. Keep MAX size of arr in hashtable as 10.

class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.Max
    
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]

    def find_slot(self, index, key):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] == None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hash is full")

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            item = self.arr[prob_index]
            if item is None:
                return None
            if item[0] == key:
                return item[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] == None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(h, key)
            self.arr[new_h] = (key, val)

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None

    
t = HashTable()
t['march 6'] = 390
t['march 7'] = 90
t['march 8'] = 10
t['march 17'] = 102
t['march 1'] = 402
t['may 2'] = 250
t['may 3'] = 270
t['may 4'] = 450
t['may 5'] = 210
t['may 6'] = 21

print(t['march 17'])
print(t.arr)

del t['may 2']
del t['may 5']
print(t.arr)
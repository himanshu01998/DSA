# Hackerrank Data Structures Questions - Tree: Huffman Decoding

import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden(): # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2] # contains root object
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

def decodeHuff(root, s):
    # "print(ip)" is simply printing the global variable that stores the input string which 
    # the driver program uses to build the Huffman tree.
    # "ip" is not one of the parameters of the "decodeHuff()" function, so this solution is 
    # obviously illegal. But it's fun ;-)

    # print(ip)


    # Real method starts here
    cur = root
    chararr = [] # For each character, If at an internal node, move left if 0, right if 1
    # If at a leaf (no children), record data and jump back to root AFTER processing character

    for c in s:
        if c == '0' and cur.left:
            cur = cur.left
        elif cur.right:
            cur = cur.right

        if cur.left is None and cur.right is None:
            chararr.append(cur.data)
            cur = root

    print("".join(chararr))


ip = input()
freq = {} # maps each character to its frequency

cntr = 0

for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

# This will create the Node for tree 
root = huffman_hidden() # contains root of huffman tree

code_hidden = {} # contains code for each object

# This will create binary num for huffman encoding 
dfs_hidden(root, "")

if len(code_hidden) == 1: # if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

# This will be used to create a Binary string for decoding 
toBeDecoded = ""

for ch in ip:
   toBeDecoded += code_hidden[ch]


decodeHuff(root, toBeDecoded)


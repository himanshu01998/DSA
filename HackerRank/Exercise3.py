# Hackerrank Data Structures Questions - Tree: Preorder, Postorder, Inorder Traversal, 
# Height of a Binary Tree, Top view, Level order Traversal

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def preOrder(root):
    if root is None:
        return
    print(root.info, end=' ')
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.info, end =" ")

def inOrder(root):
    if root.left:
        inOrder(root.left)
    print(root.info, end=" ")
    if root.right:
        inOrder(root.right)

def height(root):
    left_height = 0
    right_height = 0

    if root.left:
        left_height = 1 + height(root.left)

    if root.right:
        right_height = 1 + height(root.right)
    
    if left_height > right_height:
        return left_height
    return right_height

def topView(root):
    hm={}
    queue=[]
    queue.append((root,0))

    while(queue):
        q=queue.pop(0)
        if q[1] not in hm:
            hm[q[1]]=q[0].info
        if q[0].left:
            queue.append((q[0].left,q[1]-1))
        if q[0].right:
            queue.append((q[0].right,q[1]+1))
    
    print(hm)
    for k, v in sorted(hm.items()):
        print(str(v)+' ', end='')

def levelOrder(root):
    que = []
    que.append(root)

    while len(que) > 0:
        q = que.pop(0)
        print(q.info, end=' ')

        if q.left:
            que.append(q.left)
        if q.right:
            que.append(q.right)


tree = BinarySearchTree()
# arr = [1, 2, 5, 3, 6, 4]
arr = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]
t = len(arr)

for i in range(t):
    tree.create(arr[i])

print("Pre-Order:")
preOrder(tree.root)
print("\nPost-Order:")
postOrder(tree.root)
print("\nIn-Order:")
inOrder(tree.root)
print("\nHeight:")
print(height(tree.root))
print("\nTop View:")
topView(tree.root)
print("\nLevel:")
levelOrder(tree.root)
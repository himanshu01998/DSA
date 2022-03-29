class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, val):
        if val < self.data:
            self.left = self.left.delete(val)
        elif val > self.data:
            self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            
            # To use max element from left subtree
            max_val = self.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

            # # To use min element from right subtree 
            # min_val = self.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    obj = build_tree([15, 12, 27, 20, 88, 23, 14, 7])
    print(obj.in_order_traversal())
    obj.delete(20)
    print(obj.in_order_traversal())
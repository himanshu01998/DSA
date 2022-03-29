class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return     # Node already exists

        if data < self.data:
            # data is less than current node so add it to left side 
            if self.left:
                # if left node is not empty call recursive method and finally set left node = data
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # data is greater than current node so add it to right side
            if self.right:
                # if right node is not empty call recursive method and finally set right node = data
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(17))
    print(numbers_tree.search(178))

    country_tree = build_tree(["India","Pakistan","Germany", "USA","China","India","UK","USA"])
    print(country_tree.in_order_traversal())
    print(country_tree.search("USA"))
    print(country_tree.search("Russia"))
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        space = ' ' * self.get_level() * 3
        prefix = space + '|_' if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("Surface"))

    phone = TreeNode("Phone")
    phone.add_child(TreeNode("iPhone"))
    phone.add_child(TreeNode("Pixel"))
    phone.add_child(TreeNode("Oneplus"))
    phone.add_child(TreeNode("Samsung"))

    tv = TreeNode("Television")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(tv)
    
    root.print_tree()

build_product_tree()
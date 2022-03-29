# Build below location tree using TreeNode class
# Global
#    |__ India
#       |__ Gujarat
#          |__ Ahemdabad
#          |__ Baroda
#       |__ Karnataka
#          |__ Bengaluru
#          |__ Mysore
#    |__ USA
#       |__ New Jersey
#          |__ Princeton
#          |__ Trenton
#       |__ California
#          |__ San Francisco
#          |__ Mountain View
#          |__ Palo Alto

# Now modify print_tree method to take tree level as input. And that should print tree only 
# upto that level as shown below,
# root_node.print_tree(2)
# Global
#    |__ India
#       |__ Gujarat
#       |__ Karnataka
#    |__ USA
#       |__ New Jersey
#       |__ California


class TreeNode:
    def __init__(self, city):
        self.city = city
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return
        space = ' ' * self.get_level() * 3
        prefix = space + '|__' if self.parent else ""
        print(prefix, self.city)
        for child in self.children:
            child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_tree():
    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahemdabad"))
    gujarat.add_child(TreeNode("Baroda"))
    
    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bengaluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    jersey = TreeNode("New Jersey")
    jersey.add_child(TreeNode("Princeton"))
    jersey.add_child(TreeNode("Trenton"))

    cal = TreeNode("California")
    cal.add_child(TreeNode("San Francisco"))
    cal.add_child(TreeNode("Mountain View"))
    cal.add_child(TreeNode("Palo Alto"))

    usa.add_child(jersey)
    usa.add_child(cal)

    root = TreeNode("Global")
    root.add_child(india)
    root.add_child(usa)
    return root


if __name__ == '__main__':
    root_node = build_tree()
    root_node.print_tree(2)
    root_node.print_tree(1)
    root_node.print_tree(4)
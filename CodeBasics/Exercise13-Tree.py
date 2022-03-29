# Below is the management hierarchy of a company.
# Nilupul (CEO)
#    |__Chinmay (CTO)
#       |__Vishwa (Infrastructure Head)
#          |__Dhaval (Cloud Manager)
#          |__Abhijit (App Manager)
#       |__Aamir (Application Head)
#    |__Gels (HR Head)
#       |__Peter (Recruitement Manager)
#       |__Waqas (Policy Manager)

# Extent tree class built in our main tutorial so that it takes name and designation 
# in data part of TreeNode class. Now extend print_tree function such that it can print 
# either name tree, designation tree or name and designation tree. As shown below,
# CEO                                                                                         
#    |__CTO                                                                                   
#       |__Infrastructure Head                                                                
#          |__Cloud Manager                                                                   
#          |__App Manager                                                                     
#       |__Application Head                                                                   
#    |__HR Head                                                                               
#       |__Recruitement Manager                                                               
#       |__Policy Manager                                                                     

# Nilupul
#    |__Chinmay
#       |__Vishwa
#          |__Dhaval
#          |__Abhijit
#       |__Aamir
#    |__Gels
#       |__Peter
#       |__Waqas

# Nilupul(CEO)
#    |__Chinmay(CTO)
#       |__Vishwa(Infrastructure Head)
#          |__Dhaval(Cloud Manager)
#          |__Abhijit(App Manager)
#       |__Aamir(Application Head)
#    |__Gels(HR Head)
#       |__Peter(Recruitement Manager)
#       |__Waqas(Policy Manager)

# Here is how your main function should will look like,
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("designation") # prints only designation hierarchy
#     root_node.print_tree("both") # prints both (name and designation) hierarchy


class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, val):
        if val == "both":
            value = self.name + "(" + self.designation + ")"
        elif val == "name":
            value = self.name
        else:
            value = self.designation

        space = ' ' * self.get_level() * 3
        prefix = space + '|__' if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(val)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_tree():
    cto = TreeNode("Chinmay", "CTO")
    ih = TreeNode("Vishwa", "Infrastructure Head")
    ih.add_child(TreeNode("Dhaval", "Cloud Manager"))
    ih.add_child(TreeNode("Abhijit", "App Manager"))
    cto.add_child(ih)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    hr = TreeNode("Gels", "HR Head")
    hr.add_child(TreeNode("Peter", "Recruitement Manager"))
    hr.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo

if __name__ == "__main__":
    root_node = build_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")

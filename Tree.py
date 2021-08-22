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



    def print_tree(self,val):

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                if self.get_level()==val:
                    break
                child.print_tree(val)


    def add_child(self, child):
        child.parent = self
        self.children.append(child)




def build_product_tree():
    Global = TreeNode('Global')

    India = TreeNode("India")
    Gujarat = TreeNode("Gujarat")
    Gujarat.add_child(TreeNode("Ahmedabad"))
    Gujarat.add_child(TreeNode("Baroda"))

    Karnatka =TreeNode("KArnatka")
    Karnatka.add_child(TreeNode("Bangluru"))
    Karnatka.add_child(TreeNode("Mysore"))

    USA = TreeNode("USA")
    New_jersey = TreeNode("New Jersey")
    New_jersey.add_child(TreeNode("Princeton"))
    New_jersey.add_child(TreeNode("Trenton"))

    California = TreeNode("California")
    California.add_child(TreeNode("San Francisco"))
    California.add_child(TreeNode("Mountain View"))
    California.add_child(TreeNode("Palo Alto"))

    Global.add_child(India)
    Global.add_child(USA)
    India.add_child(Gujarat)
    India.add_child(Karnatka)
    USA.add_child(New_jersey)
    USA.add_child(California)

    return Global


if __name__ == '__main__':
    root=build_product_tree()
    root.print_tree(3)
    

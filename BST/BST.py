class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right =None

    def add_child(self,data):
        if data==self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)


        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def inorder_traversal(self):
        elements =[]
        if self.left:
            elements+=self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements+=self.right.inorder_traversal()

        return elements

    def search(self,val):
        if val == self.data:
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


    def find_min(self):
        return self.left.inorder_traversal()[0]

    def find_max(self):
        return self.right.inorder_traversal()[-1]

    def calculate_sum(self):
        sum=0
        if self.left:
            for i in self.left.inorder_traversal():
                sum+=i

        sum+= self.data

        if self.right:
            for j in self.right.inorder_traversal():
                sum+=j


        return sum


    def postorder_traversal(self):
        elements =[]
        if self.left:
            elements+=self.left.postorder_traversal()

        if self.right:
            elements +=self.right.postorder_traversal()

        elements.append(self.data)

        return elements


    def preorder_traversal(self):
        elements=[]

        elements.append(self.data)

        if self.left:
            elements+=self.left.preorder_traversal()

        if self.right:
            elements+= self.right.preorder_traversal()

        return elements

def build_tree(elem):
    root = BSTNode(elem[0])

    for i in range(1,len(elem)):
        root.add_child(elem[i])
    return root


 
if __name__=='__main__':
    countries=['India','UK','sweden','Bharat']
    country_tree = build_tree(countries)
    print(country_tree.inorder_traversal())
    print(country_tree.search('sweden'))

    numbers = [17,4,1,20,9,23,18,34,18,4]
    numbers_tree = build_tree(numbers)
    print('inorder_traversal:')
    print(numbers_tree.inorder_traversal())
    print('search numerical_value')
    print(numbers_tree.search(180))
    print('Minimum value')
    print(numbers_tree.find_min())
    print('Maximum value')
    print(numbers_tree.find_max())
    print('Sum of all values in Tree:')
    print(numbers_tree.calculate_sum())
    print('Postorder traversal')
    print(numbers_tree.postorder_traversal())
    print('preorder_traversal')
    print(numbers_tree.preorder_traversal())


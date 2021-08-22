'Add node in Linkedlist is linkedlist is empty'


class Node:
	def __init__(self,data):
		self.data =data
		self.next =None

class linkedlist:
	def __init__(self):
		self.head=None

	def printlist(self):
		temp =self.head
		while temp:
			print(temp.data)
			temp = temp.next

	

	def add_node(self,node):
		self.head = node
		return True
		if self.head!= None:
			return self.add_node(node)






if __name__=="__main__":
	linklist = linkedlist()

	linklist.head = Node(1)
	second = Node(2)
	third =Node(3)

	linklist.head.next =second
	second.next = third

	#linklist.printlist()
	linklist.printlist()
	linklist.add_node(Node(5))
	
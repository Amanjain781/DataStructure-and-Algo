

class Node:
	'Create Node for Singly LinkedList'
	def __init__(self,data):
		self.data =data
		self.next =None

class linkedlist:
	'For linkedlist Operatios like create linkedlist,traverse and add_node.'
	def __init__(self):
		self.head=None


	def printlist(self):
		'Traverse and Print LinkedList'
		temp =self.head
		while temp:
			print(temp.data,'-->',end=' ')
			temp = temp.next

	

	def add_node(self,new_node,pos=None,prev_node=None):
		'Add node on a after a specific node or any specific position'
		self.new_node=new_node
		if pos==0:
			self.new_node.next = self.head
			self.head = self.new_node
		elif pos=='last':
			if self.head:
				last = self.head
				while(last.next):
					last = last.next
				last.next = self.new_node
			else:
				self.head = self.new_node

		else:
			if prev_node == None:
				print('please enter previous node value')
				return

			else:
				pos=None
				self.new_node.next = prev_node.next
				prev_node.next = self.new_node





if __name__=="__main__":
	linklist = linkedlist()

	linklist.head = Node(1)
	second = Node(2)
	third =Node(3)

	linklist.head.next =second
	second.next = third

	#linklist.printlist()
	#print('After adding one parameter')
	#linklist.add_node(Node(6),pos='last')
	#linklist.add_node(Node(5),prev_node=linklist.head.next.next)
	linklist.printlist()
	#print(linklist.search(2))
	linklist.printlist()
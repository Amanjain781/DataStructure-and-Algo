'Search node position in linkedlist'

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

	def search(self,val):
		self.pos=0
		temp =self.head
		while temp:
			if val == temp.data:
				return temp.data
				break
			temp = temp.next
			self.pos+=1


	def add_node(self,new_node,pos=None,prev_node=None):
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

	linklist.printlist()
	#print('After adding one parameter')
	#linklist.add_node(Node(6),pos='last')
	#linklist.add_node(Node(5),prev_node=linklist.head.next.next)
	#linklist.printlist()
	#print(linklist.search(2))

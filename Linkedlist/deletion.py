class Node:
	def __init__(self,data):
		self.data =data
		self.prev = None
		self.next =None

class linkedlist:
	def __init__(self):
		self.head=None

	def printlist(self):
		temp =self.head
		while temp:
			print(temp.data)
			temp = temp.next

	def nodes(self,position):
		pos=0
		temp =self.head
		while temp:
			if pos == position:
				return prev_node,temp
			prev_node = temp
			temp = temp.next
			pos+=1


	def deleteNode(self,key):
		temp =self.head
		if temp:
			# if key hold by head value
			if key == temp.data:
				self.head=temp.next
				return self.printlist()
			else:		
				# if key not in head
				while temp:
					if key == temp.data:
						prev_node.next = temp.next
						return self.printlist()
					prev_node = temp
					temp = temp.next
					

	def deleteNodePos(self,node_pos):
		temp =self.head
		# if position of node is 0 
		
		if node_pos==0:
			prim =temp.next
			self.head = prim
			return self.printlist()
		else:
			#for other nodes
			prev,node = self.nodes(node_pos)
			prev.next = node.next
			return self.printlist()

if __name__=="__main__":
	linklist = linkedlist()

	linklist.head = Node(1)
	second = Node(5)
	third =Node(8)

	linklist.head.next =second
	second.next = third
	#linklist.deleteNode(8)
	#linklist.printlist()
	linklist.deleteNodePos(4)
	
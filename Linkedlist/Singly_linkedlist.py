'''
Linked List deletion and length of linked list using iterative and recursion
'''



class Node:
	def __init__(self,data):
		self.data =data
		self.next =None

class linkedlist:
	def __init__(self):
		self.head=None

	# print Linkedlist
	def printlist(self):
		temp =self.head
		while temp:
			print(temp.data)
			temp = temp.next

	# delete linkedlist
	def deletelinklist(self):
		if self.head == None:
			print('It is already empty')
		else:
			self.head = None
			print('Linklist is deleted')
			return self.printlist()


	def length(self):
		# print length of Linked List
		# using iterative approach
		count = 0
		temp =self.head
		while temp:
			count+=1
			temp=temp.next
		return count

	def getCountRec(self, node):
		# get count of linked list 
		if (not node): # Base case
			return 0
		else:
			return 1 + self.getCountRec(node.next)
 
    # A wrapper over getCountRec()
	def getCount(self):
		return self.getCountRec(self.head)


if __name__=="__main__":
	linklist = linkedlist()

	linklist.head = Node(1)
	second = Node(5)
	third =Node(8)

	linklist.head.next =second
	second.next = third
	#linklist.deleteNode(8)
	#linklist.printlist()
	#linklist.printlist()
	#linklist.deletelinklist()
	print(linklist.getCount())
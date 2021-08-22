'''
Find Nth node,length of linked list,find middle nodeand count the values in linked lists
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


	def nth_node(self,index_val):
		# for finding nth number of node
		count = 0
		node = self.head
		while node:
			if count == index_val:
				return node.data
			node = node.next
			count+=1

	def nth_back(self,index_val):
		# print nth value from th end of a linked list
		length = 0
		node = self.head
		while node:
			length+=1
			node = node.next

		if index_val > length:
			print('given value is greater than length of Linked list')


		node = self.head
		for i in range(length - index_val,0-1):
			node = node.next
		print(node.data)


	def length(self):
		# for finding length of linked list
		length = 0
		node = self.head
		while node:
			length+=1
			node = node.next
		return length

	def middle_node(self):
		# for finding middle node of linked list
		val = self.length()%2

		if val!=0:
			# for odd value of length 
			val+=1
			node =self.head
			for i in range(val):
				node= node.next
			return (node.data)
		else:
			# for even value of length
			node = self.head
			for i in range(val):
				node = node.next
			return (node.data)

	def count_int(self):
		# counts the number of times a given int occurs in a Linked List
		val=0
		count =0

		node = self.head
		while node:
			if node.data == val:
				count+=1
				print(' value is',val,'with count',count)
			else:
				val = node.data
				count=1
				print(' value is',val,'with count',count)
			node = node.next


if __name__=="__main__":
	linklist = linkedlist()

	linklist.head = Node(1)
	second = Node(5)
	third =Node(8)

	linklist.head.next =second
	second.next = third

	#linklist.printlist()
	#linklist.nth_back(0)
	#print(linklist.middle_node())
	linklist.count_int()
class Node:
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.ref = None

class D_linkedlist:
	def __init__(self):
		self.head=None


	def F_traversal(self):
		if self.head is None:
			print('Linkedlist is Empty!')
		else:
			temp =self.head
			while temp:
				print(temp.data,'-->',end=' ')
				temp = temp.ref

	def B_traversal(self):
		'Linkedlist traversal in Backward'
		'or we can say print linkedlist in Backward direction'

		if self.head is None:
			print('Linkedlist is Empty!')

		else:
			n = self.head
			while n.ref is not None:
				n = n.ref

			while n.prev is not None:
				print(n.data,'-->',end=' ')
				n= n.prev



if __name__ == '__main__':
	ll = D_linkedlist()
	ll.F_traversal()
	ll.B_traversal()
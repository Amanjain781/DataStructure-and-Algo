class Node(object):
  'This class helps for creating Node'
  def __init__(self,data):
    self.data =data
    self.ref = None

class linkedlist:
  'linkedlist class helps to create linkedlist,add element,delete element etc.'
  def __init__(self):
    self.head = None

  # add element in empty LinkedList
  def add(self,data):
    if self.head == None:
      new_node = Node(data)
      new_node.ref = self.head
    else:
      print('Linked List Should be empty!')

  # add element at beginning
  def add_begin(self,data):
    new_node = Node(data)
    new_node.ref = self.head
    self.head = new_node

  # add elements at end  
  def add_end(self,data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    n = self.head
    while n.ref is not None:
      n = n.ref
    n.ref = new_node

  # add node after a specific node
  def add_after(self,data,x):
    new_node = Node(data)
    n = self.head
    while n is not None:
      if x == n.data:
        break
      n = n.ref
    if n is None:
      print('Item not present in list')
    else:
      new_node = Node(data)
      new_node.ref = n.ref
      n.ref = new_node 
  # add new Node before a specific Node
  def add_before(self,data,x):
    # if head is empty of Linked List
    if self.head is None:
      print('Linked list is Empty!')
      return

    # If we have to add node before first node
    if self.head.data==x:
      new_node = Node(data)
      new_node.ref = self.head
      self.head = new_node

    n = self.head
    while n.ref is not None:
      if n.ref.data == x:
        break
      n = n.ref

    if n.ref is None:
      print('Node is not Found')

    else:
      new_node = Node(data)
      new_node.ref = n.ref
      n.ref = new_node

  # for print linkedlist
  def traverse(self):
    if self.head ==None:
      print('Linkedlist is Empty!')
    else:
      n = self.head
      while n is not None:
        print(n.data,'--->',end=' ')
        n = n.ref


if __name__ == '__main__':
  LL1 = linkedlist()  
  LL1.add_begin(9)
  LL1.add_end(4)
  LL1.add_begin(10)
  LL1.add_before(100,4)
  LL1.add_after(200,8)


  LL1.traverse()



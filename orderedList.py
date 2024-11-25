class Node:
  next = None

  def __init__(self, data):
    self.data = data

class sortedLinkedList:

  def __init__(self):
    self.__head = None
    self.__tail = None

  def add(self, newNode):
    #se lista vuota
    if(self.__head is None):
      self.__head = newNode
      self.__tail = self.__head
      return
    #se inserisco in testa
    if(self.__head.data <= newNode.data):
      if(self.__head.data == newNode.data):
        return
      newNode.next = self.__head
      self.__head = newNode
      return
    #se inserisco in coda
    if(self.__tail.data >= newNode.data):
      if(self.__tail.data == newNode.data):
        return
      self.__tail.next = newNode
      self.__tail = newNode
      return
    #se inserisco al centro
    p = self.__head
    while(p.next != None and (p.next.data >= newNode.data)):
      p = p.next
    if(p.next.data == newNode.data):
        return
    newNode.next = p.next
    p.next = newNode

  def printPath(self):
    p = self.__head
    while(p != None):
      print(f"-> {p.data}")
      p = p.next

lista = sortedLinkedList()
lista.add(Node(2))
lista.add(Node(2))
lista.add(Node(1))
lista.add(Node(1))
lista.add(Node(4))
lista.add(Node(4))
lista.add(Node(4))
lista.add(Node(3))
lista.printPath()




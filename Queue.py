class Node:
  next = None

  def __init__(self, data):
    self.data = data

class Queue:

  def __init__(self):
    self.__head = None
    self.__tail = None

  #inserimento
  def enqueue(self, newNode):
    #se coda vuota
    if(self.__head is None):
      self.__head = newNode
      self.__tail = self.__head
      return
    self.__tail.next = newNode
    self.__tail = newNode

  #rimozione
  def dequeue(self):
    #se coda vuota
    if(self.__head is None):
      return
    #se coda con un solo elemento
    if(self.__head == self.__tail):
      self.__head = None
      self.__tail = None
      return
    #se coda non vuota
    p = self.__head
    self.__head = self.__head.next
    p.next = None
    return p

  def printPath(self):
    p = self.__head
    while(p != None):
      print(f"-> {p.data}", end =" ")
      p = p.next

lista = Queue()
lista.enqueue(Node(1))
lista.enqueue(Node(2))
lista.enqueue(Node(3))
lista.enqueue(Node(4))
lista.printPath()
lista.dequeue()
lista.dequeue()
print(f"\n")
lista.printPath()
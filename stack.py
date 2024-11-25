class Node:
  next = None

  def __init__(self, data):
    self.data = data

class Stack:

  def __init__(self):
    self.__head = None
    self.__tail = None

  def push(self, newNode):
    #inserimento in testa
    newNode.next = self.__head
    self.__head = newNode

  def pop(self):
    #se pila vuoto
    if(self.__head is None):
      return
    #rimozione in testa
    p = self.__head
    self.__head = self.__head.next
    p.next = None
    return p

  def printPath(self):
    p = self.__head
    while(p != None):
      print(f"-> {p.data}", end =" ")
      p = p.next

lista = Stack()
lista.push(Node(1))
lista.push(Node(2))
lista.push(Node(3))
lista.push(Node(4))
lista.printPath()
lista.pop()
lista.pop()
print(f"\n")
lista.printPath()
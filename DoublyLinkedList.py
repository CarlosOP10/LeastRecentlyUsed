#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
from Node import Node

class DoublyLinkedList:
  def __init__(self,sizeOfList):
    self.first=None
    self.latest=None
    self.sizeOfList=sizeOfList
    self.count=0
    self.elements=set()

  def insertEnd(self,value):
    newNode=Node(value)
    if value not in self.elements:
      if self.first==None:
        self.first=newNode
        self.latest=newNode
        self.elements.add(value)
        self.count+=1
      else:
        if self.count==self.sizeOfList:
          self.deleteFist()
          self.insertEnd(value)
        else:
          self.latest.next=newNode
          newNode.previous=self.latest
          self.latest=newNode
          self.elements.add(value)
          self.count+=1
  
  def deleteFist(self):
    value=''
    if self.first!=None:
      if self.first!=self.latest:
        value=self.first.value
        self.first=self.first.next
        self.first.previous=None
        self.elements.remove(value)
        self.count-=1
      else:
        value=self.first.value
        self.first=None
        self.latest=None
        self.elements.remove(value)
        self.count=0
    else:
      print("Lista Vacia")
    return value

  def getItem(self,value):
    nodeAux=self.first
    findValue=False
    valueFind=''
    if nodeAux!=None:
      if nodeAux.value==value:
        valueFind=self.deleteFist()
        self.insertEnd(valueFind)
        return valueFind

      elif self.latest.value==value:
        return self.latest.value
      else:
        nodeAux=nodeAux.next
        while not findValue and nodeAux!=None:
          if(nodeAux.value==value):
            findValue=True
            valueFind=nodeAux.value
            nodeAux.previous.next=nodeAux.next
            nodeAux.next.previous=nodeAux.previous
            self.count-=1
            self.elements.remove(valueFind)
            self.insertEnd(valueFind)
          else:
            nodeAux=nodeAux.next
    else:
      print('Lista Vacia')
    return valueFind



  def showList(self):
    nodeAux=self.first
    while nodeAux!=None:
      print(nodeAux.value,end=' ')
      nodeAux=nodeAux.next
    print()
    
  def getItems(self):
    nodeAux=self.first
    items=[]
    while nodeAux!=None:
      items.append(nodeAux.value)
      nodeAux=nodeAux.next
    return items


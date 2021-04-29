#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
from Node import Node

class DoublyLinkedList:
  def __init__(self,sizeOfList):
    self.first=None
    self.latest=None
    self.sizeOfList=sizeOfList
    self.count=0

  def insertEnd(self,value):
    newNode=Node(value)
    if self.first==None:
      self.first=newNode
      self.latest=newNode
      self.count+=1
    else:
      if self.count==self.sizeOfList:
        self.deleteFist()
        self.insertEnd(value)
      else:
        self.latest.next=newNode
        newNode.previous=self.latest
        self.latest=newNode
        self.count+=1
  
  def deleteFist(self):
    value=''
    if self.first!=None:
      if self.first!=self.latest:
        value=self.first.value
        self.first=self.first.next
        self.first.previous=None
        self.count-=1
      else:
        value=self.first.value
        self.first=None
        self.latest=None
        self.count=0
    else:
      print("Lista Vacia")
    return value

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


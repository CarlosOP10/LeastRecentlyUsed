#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
from DoublyLinkedList import DoublyLinkedList
from os import system
import copy 

listLinked=DoublyLinkedList(3)

option=1
while option!='0':
  system("clear")
  print('1. Insert End')
  print('2. Delete First')
  print('3. Show List')
  print('0. Exit')
  option=input("Enter the option: ")
  if option=='1':
    value=int(input('Enter the value: '))
    listLinked.insertEnd(value)
  elif option=='2':
    listLinked.deleteFist()
  elif option=='3':
    listLinked.showList()
    input("Press the <ENTER> key to continue...")







#copy objets
# ex2 = copy.deepcopy(ex)
# ex2.insertEnd(4)
# ex.showList()
# ex2.showList()
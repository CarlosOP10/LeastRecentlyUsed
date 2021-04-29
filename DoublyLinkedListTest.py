#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import unittest
from DoublyLinkedList import DoublyLinkedList

class TestDoublyLinkedListMethods(unittest.TestCase):

  def setUp(self):
    self.linkedList=DoublyLinkedList(2)
    self.likedListDelete=DoublyLinkedList(2)
    self.likedListDelete.insertEnd(1)
    self.likedListDelete.insertEnd(2)

  def testCreateDoublyListLinkedFirst(self):
    self.assertEqual(self.linkedList.first, None)

  def testCreateDoublyListLinkedLatest(self):
    self.assertEqual(self.linkedList.latest, None)
  
  def testInsertEnd(self):
    linkendList=DoublyLinkedList(2)
    linkendList.insertEnd(4)
    self.assertEqual(linkendList.latest.value,4)
    
  def testInsertEndWith2Values(self):
    linkendList=DoublyLinkedList(3)
    linkendList.insertEnd(4)
    linkendList.insertEnd(2)
    self.assertEqual(linkendList.latest.value,2)

  def testInsertEndWith3Values(self):
    linkendList=DoublyLinkedList(2)
    linkendList.insertEnd(4)
    linkendList.insertEnd(2)
    linkendList.insertEnd(1)
    self.assertEqual(linkendList.latest.value,1)

  def testInsertEndExceedingMaximumSize(self):
    linkendList=DoublyLinkedList(3)
    linkendList.insertEnd(1)
    linkendList.insertEnd(2)
    linkendList.insertEnd(3)
    linkendList.insertEnd(4)
    self.assertEqual(linkendList.getItems(),[2,3,4])

  def testInsertEndExceedingMaximumSizeWith2Items(self):
    linkendList=DoublyLinkedList(3)
    linkendList.insertEnd(1)
    linkendList.insertEnd(2)
    linkendList.insertEnd(3)
    linkendList.insertEnd(4)
    linkendList.insertEnd(5)
    self.assertEqual(linkendList.getItems(),[3,4,5])

  def testDeleteFirstLinkedList(self):
    self.likedListDelete.deleteFist()
    self.assertEqual(self.likedListDelete.first.value,2)

  def testDelete2ItemsFirstLinkedList(self):
    self.likedListDelete.deleteFist()
    self.likedListDelete.deleteFist()
    self.assertEqual(self.likedListDelete.first,None)

  def testDeleteEmptyLinkedList(self):
    linkedList=DoublyLinkedList(2)
    self.assertEqual(linkedList.deleteFist(),'')

if __name__ == '__main__':
  unittest.main()

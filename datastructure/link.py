from .base import SingleLink,Node
from .exceptions import LinkedListException

class LCList():
    '''
    循环单链表
    '''
    def __init__(self,node = None):
        self._rear = node

    def prepend(self,item):
        node = Node(item)
        rear = self._rear
        head = rear.next
        rear.next,node.next = node,head

    def append(self,item):
        node = Node(item)
        rear = self._rear
        head = rear.next
        rear.next,node.next = node,head
        self._rear = node

    def pop(self):
        if self._rear is None:
            raise LinkedListException('in pop')
        rear = self._rear
        head = rear.next
        if rear is head:
            self._rear = None
        else:




    def printall(self):
        pass
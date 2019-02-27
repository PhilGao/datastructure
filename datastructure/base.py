# -*- coding: utf-8 -*-

"""
datastructure.base
~~~~~~~~~~~~~

This module contains base class definition ,including Node , SingleLink
"""
from .exceptions import LinkedListException

class Node():
    '''base class of node '''
    def __init__(self, item, next=None):
        '''
        Init a node
        :param item: node value
        :param next: next node , default is None
        '''
        self.item = item
        self.next = next


class SingleLink(object):
    '''base class of SingleLink '''
    def __init__(self, node=None):
        '''
        init a single link
        :param node: Node
        '''
        self._head = node

    def is_empty(self):
        '''
        check singlelist is empty or not
        :return:
        '''
        return self._head is None

    def prepend(self, item):
        '''
        add node at header
        :param item: value
        :return: None
        '''
        node = Node(item)
        cur = self._head
        self._head, node.next = node, cur

    def pop(self):
        '''
        pop the header
        :return:
        '''
        if self._head is None:
            raise LinkedListException("in pop")
        item = self._head.item
        self._head = self._head.next
        return item

    def append(self, item):
        '''
        append node at tail
        :param item: value
        :return: None
        '''
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def pop_last(self):
        '''
        pop the last value
        :return:
        '''
        if self._head is None:
            raise LinkedListException('in pop_last')
        cur = self._head
        if cur.next is None:
            self._head = None
            return cur.item
        while cur.next.next:
            cur = cur.next
        item = cur.next.item
        cur.next = None
        return item

    def find(self, pred):
        '''
        find first element meet the predicate
        :param pred: We use the term predicate to mean any Python function that tests some condition and returns a Boolean value. For example, x < y is a predicate that tests whether x is less than y. For example, 5 < 500 returns True, while 5 >= 500 returns False.
        :return: item
        '''
        cur = self._head
        while cur.next:
            if pred(cur.item):
                return cur.item
            cur = cur.next

    def printall(self):
        '''
        print all the element
        :return:
        '''
        cur = self._head
        while cur:
            print(cur.item,end='')
            cur = cur.next
            if cur:
                print(',',end='')
        print('')

    def elements(self):
        '''
        get all element of the link
        :return: generator
        '''
        cur = self._head
        while cur:
            yield cur.item
            cur = cur.next

    def for_each(self,proc):
        '''
        apply proc function to each item in list
        :param proc: function
        :return:
        '''
        cur = self._head
        while cur:
            proc(cur)
            cur = cur.next


    def filter(self,pred):
        '''
        find all element meet the predicate
        :param pred: We use the term predicate to mean any Python function that tests some condition and returns a Boolean value. For example, x < y is a predicate that tests whether x is less than y. For example, 5 < 500 returns True, while 5 >= 500 returns False.
        :return: generator
        '''
        cur = self._head
        while cur.next:
            if pred(cur.item):
                yield cur.item
            cur = cur.next

    #below all function are not aborted

    def travel(self):
        '''
        travel the single list , print each node' item
        :return: None
        '''
        if self.is_empty():
            print('travel : empty list')
            return
        else:
            cur = self._head
            while cur:
                print('travel:', cur.item)
                cur = cur.next
            return

    def len(self):
        '''
        length of single list
        :return: int length
        '''
        cur = self._head
        count = 0
        if self.is_empty():
            # print('len:',count)
            return 0
        else:
            while cur:
                count += 1
                cur = cur.next
            # print('len:',count)
            return count

    def insert(self, item, index):
        '''
        Insert one item at given index
        :param item: value
        :param index: index , start from 0
        :return:
        '''
        node = Node(item)
        cur = self._head
        count = 1
        if index >= self.len():
            self.append(item)
            return
        else:
            while count < index:
                cur = cur.next
                count += 1
            cur.next, node.next = node, cur.next
            return

    def remove(self, item):
        '''
        remove one value from singlelist
        :param item: value
        :return:
        '''
        cur = self._head
        if not cur or cur.item == item:
            self._head = None
        else:
            while cur.next:
                pre = cur
                cur = cur.next
                if cur.item == item:
                    pre.next = cur.next
                    return
        print('Not found')
        return

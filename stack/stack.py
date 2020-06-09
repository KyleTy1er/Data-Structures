"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   When using an array we can use append and pop, but with the Linked List
   we have to follow the Class constraints of head and tail values.

"""

import sys

sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def push(self, value):
        self.size = len(self.storage)
        self.storage.append(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            return self.storage.pop()

    def len(self):
        self.size = len(self.storage)
        return self.size



class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.storage.remove_tail()

    def len(self):
        return self.size
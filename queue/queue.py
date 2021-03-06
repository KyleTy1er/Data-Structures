"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   Using an array the storage is an empty list that we can add to or take from
   with built in Python methods such as append and pop...
   Using the Linked List the storage involves a head and a tail, and the
   functionality of adding and removing is constrained by the head and
   tail values to keep the order of the Linked List. In an array you can
   access locations with a single operation through index, whereas with
   a Linked List you must iterate to find values o(n).
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# 1. Implement the Queue class using an array as the underlying storage structure.
#    Make sure the Queue tests pass.

# Queues
#
# Has the methods: enqueue, dequeue, and len.
# enqueue adds an element to the back of the queue.
# dequeue removes and returns the element at the front of the queue.
# len returns the number of elements in the queue.

# class Queue:
#
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         self.size = len(self.storage)
#         return self.size
#
#     def enqueue(self, value):
#         return self.storage.append(value)
#
#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop(0)

import sys
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from singly_linked_list.singly_linked_list import LinkedList, Node

# 2. Re-implement the Queue class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Queue tests pass.

class Queue:

    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size >= 1:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return None




# ex = Queue()
#
# ex.enqueue(39)
# ex.enqueue(3)
# ex.enqueue(6)
#
# print(ex.__len__())
# print(ex.storage.get_max())
#
# ex.dequeue()
#
# print(ex.__len__())
# print(ex.storage.get_max())
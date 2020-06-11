"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


import sys

sys.path.append('../stack')
sys.path.append('../queue')

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
    #1. check if there is no root,
        # we can check this by seeing if self == None
        # if there isn't we create the node and park it

    #2. otherwise, there is a root
        # compare value to the roots value
        # if less than go left
        # if greater or equal go right

        if value < self.value:
            # go left
            # we have to cvheck if there is another node on the left side
            # so we dont overwrite
            if self.left:
                # self.left is a node..
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            #go right
            # we have to cvheck if there is another node on the left side
            # so we dont overwrite
            if self.right:
                # self.right is already a node...
                self.right.insert(value)
            else:
                self.right = BSTNode(value)




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
      # Is there a node to check? If not return False...
        if self.value is None:
            return False
        else:
          # If the root nodes value is your target return True:
            if self.value == target:
                return True
            # if target is less than the parent node then
            # we check the left value of the child node:
            if target < self.value:
              if self.left:
                # if left child node exists:
                # if left child node contains target return True:
                if self.left.contains(target):
                    return True
                   # if at the end no variable equals the target we can return false:
                else: return False
            # if target is greater than or equal to the parent node:
            if target >= self.value:
              # if a child node on the right exists:
              if self.right:
                # check if the child node equals the target variable.
                if self.right.contains(target):
                    return True
                    # if at the end no variable equals the target we can return false:
                else: return False



    # Return the maximum value found in the tree
    def get_max(self):
      if self is None:
          return "Tree is empty."
      else:
          if self.right is None:
              return self.value
          else:
              return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
      fn(self.value)
      if self.left:
        self.left.for_each(fn)
      if self.right:
        self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        storage = Queue()
        storage.put(node)

        while storage.qsize() > 0:
            node = storage.get()
            print(node.value)

            if node.left:
                storage.put(node.left)
            if node.right:
                storage.put(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        storage = Stack()
        storage.push(node)

        while storage.size > 0:
            node = storage.pop()
            print(node.value)

            if node.left:
                storage.push(node.left)
            if node.right:
                storage.push(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass
    #
    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass

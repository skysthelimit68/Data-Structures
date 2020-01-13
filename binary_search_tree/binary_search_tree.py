import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # if there is no left child
            if not self.left:
                self.left = BinarySearchTree(value)
            # if there is left child, recursion
            else:
                self.left.insert(value)
        else:
            # if there is no right child
            if not self.right:
                self.right = BinarySearchTree(value)
            # if there is right child, recursion
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value and self.left:
            #if left child exist
            return self.left.contains(target)
            # if not self.left:
            #     return False
            # else:
            #     return self.left.contains(target)
        if target > self.value and self.right:
            #if right child does exist
            return self.right.contains(target)
            # if not self.right:
            #     return False
            # else:
            #     return self.right.contains(target)

        return False
    # Return the maximum value found in the tree
    def get_max(self):
        # max value is either self or from one of it's right children as left children are all smaller than self
        # SO ...  we are trying to find the MOST OUTTER RIGHT child in the tree
        
        # is this an empty tree?
        if not self:
            return None

        # if there are no right child
        if not self.right:
            return self.value
        
        self.right.get_max()



    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        #start from left child first, then print, then right child, from low to high
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

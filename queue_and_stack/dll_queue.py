import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()      # creating an empty list
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        #add to back
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        #remove from front
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size

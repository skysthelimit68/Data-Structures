"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

        # new_next = self.next
        # new_node = ListNode(value, self, new_next)
        # self.next = new_node
        # if new_next:
        #     new_next.prev = new_node

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

        # new_prev = self.prev
        # new_node = ListNode(value, new_prev, self)
        # self.prev = new_node
        # if new_prev:
        #     new_prev.next = new_node

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next        

        # if self.prev:
        #     self.prev.next = self.next
        # if self.next:
        #     self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        current_head = self.head
        self.head = ListNode(value, None, current_head)
        if current_head:
            current_head.prev = self.head
        else:
            self.tail = self.head

        self.length += 1

        # old_head = self.head
        # if self.head:
        #     old_head.insert_before(value)
        #     self.head = old_head.prev
        # else:
        #     self.head = ListNode(value, None, None)
        #     self.tail = self.head
        
        # self.length += 1

    """Removes the List's 
    current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        current_head = self.head
        self.head = current_head.next
        if self.length == 1:
            self.tail = self.head  # head and tail are all none
            self.length -= 1
        elif self.length > 1:
            self.head.prev = None
            self.length -= 1
        return current_head.value

        # current_head = self.head
        # self.head = current_head.next
        # self.head.prev = None
        # self.length -= 1
        # return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        current_tail = self.tail
        self.tail = ListNode(value, current_tail, None)
        if current_tail:
            current_tail.next = self.tail
        else:
            self.head = self.tail
        
        self.length += 1

        # old_tail = self.tail
        # old_tail.insert_after(value)
        # self.tail = old_tail.next
        # self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        current_tail = self.tail
        self.tail = current_tail.prev
        if self.length == 1:
            self.head = self.tail       # both are None
            self.length -= 1
        elif self.length > 1:
            self.tail.next = None
            self.length -= 1
        return current_tail.value

        # current_tail = self.tail
        # self.tail = current_tail.prev
        # self.tail.next = None
        # self.length -= 1
        # return current_tail.value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.length > 1:

            #switching the prev and next pointer 
            node.delete()
            
            if self.tail is node:
                self.tail = node.prev

            current_head = self.head
            self.head = node
            self.head.next = current_head
            self.head.prev = None
            if current_head:
                current_head.prev = self.head
        


        # old_prev = node.prev
        # old_next = node.next
        # old_next.prev = old_prev
        # old_prev.next = old_next

        # old_head = self.head
        # old_head.prev = node
        # self.head = node
        # self.head.prev = None
        # self.head.next = old_head


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # switching the prev and next pointer
        if self.length > 1:
            node.delete()

            if self.head is node:
                self.head = node.next

            current_tail = self.tail
            self.tail = node
            self.tail.prev = current_tail
            self.tail.next = None
            if current_tail:
                current_tail.next = self.tail
        

        # old_prev = node.prev
        # old_next = node.next
        # old_next.prev = old_prev
        # old_prev.next = old_next

        # old_tail = self.tail
        # old_tail.next = node
        # self.tail = node
        # self.tail.prev = old_tail
        # self.tail.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node:
            if self.head is node:
                self.head = node.next
            if self.tail is node:
                self.tail = node.prev
            node.delete()
            self.length -= 1


        # current_node = node
        # #test for head
        # if node.prev == None:
        #     self.head = current_node.next
        #     self.head.prev = None

        # #test for tail
        # elif node.next == None:
        #     self.tail = current_node.prev
        #     self.tail.next = None
        # #rest
        # else:
        #     old_prev = current_node.prev
        #     old_next = current_node.next
        #     old_prev.next = old_next
        #     old_next.prev = old_prev

        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current_node = self.head
        max_val = current_node.value
        while current_node.next:
            current_node = current_node.next
            if current_node.value > max_val:
                max_val = current_node.value        
        return max_val



"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        current_head = self.head
        self.head = ListNode(value, None, current_head)
        if current_head:
            current_head.prev = self.head
        else:
            self.tail = self.head

        self.length += 1

    def remove_from_head(self):
        current_head = self.head
        self.head = current_head.next
        if self.length == 1:
            self.tail = self.head  # head and tail are all none
            self.length -= 1
        elif self.length > 1:
            self.head.prev = None
            self.length -= 1
        return current_head.value

    def add_to_tail(self, value):
        current_tail = self.tail
        self.tail = ListNode(value, current_tail, None)
        if current_tail:
            current_tail.next = self.tail
        else:
            self.head = self.tail
        
        self.length += 1

    def remove_from_tail(self):
        current_tail = self.tail
        self.tail = current_tail.prev
        if self.length == 1:
            self.head = self.tail       # both are None
            self.length -= 1
        elif self.length > 1:
            self.tail.next = None
            self.length -= 1
        return current_tail.value

    def move_to_front(self, node):
        if self.length > 1:

            #switching the prev and next pointer 
            node.delete()
            
            if self.tail is node:
                self.tail = node.prev

            current_head = self.head
            self.head = node
            self.head.next = current_head
            self.head.prev = None
            if current_head:
                current_head.prev = self.head

    def move_to_end(self, node):
        if self.length > 1:
            node.delete()

            if self.head is node:
                self.head = node.next

            current_tail = self.tail
            self.tail = node
            self.tail.prev = current_tail
            self.tail.next = None
            if current_tail:
                current_tail.next = self.tail

    def delete(self, node):
        if node:
            if self.head is node:
                self.head = node.next
            if self.tail is node:
                self.tail = node.prev
            node.delete()
            self.length -= 1

    def get_max(self):
        current_node = self.head
        max_val = current_node.value
        while current_node.next:
            current_node = current_node.next
            if current_node.value > max_val:
                max_val = current_node.value        
        return max_val

class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def __str__(self):
    return str(self.value)

  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print(self):
      curr_node = self.head
      print(curr_node)
      while curr_node.next is not None:
        curr_node = curr_node.next
        print(curr_node)

    def add_to_head(self, value):
      new_node = ListNode(value)  
      self.length += 1
      # this is the first element in the list
      if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
      else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node 

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
      new_node = ListNode(value) 
      self.length += 1
      if not self.head and not self.tail:
        self.head = new_node
        self.tail = new_node
      else:
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        if node is self.head:
          return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        if node is self.tail:
          return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        if not self.head and not self.tail:
          return
        if self.head == self.tail:
          self.head = None
          self.tail = None
          self.length -=1
        elif self.head == node:
          self.head = node.next
          self.length -= 1
          node.delete()
        elif self.tail == node:
          self.tail = node.prev
          self.length -= 1
          node.delete()
        else:
          self.length -= 1
          node.delete()
          
    def get_max(self):
        if self.length == 0:
          return 0
        else:
          current_node = self.head
          max_val = current_node.value
          while current_node.next:
              current_node = current_node.next
              if current_node.value > max_val:
                  max_val = current_node.value        
          return max_val

   
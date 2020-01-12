from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        #creating empty DLL
        self.storage = DoublyLinkedList()       
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        current = self.storage.head
        if self.size == 1:
            if key in current.value:
                return current.value[key]
        elif self.size > 1:
            while current.next:
                current = current.next
                if key in current.value:
                    self.storage.move_to_front(current)
                    return current.value[key]
                else:
                    return None
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # need to check for 
        # 1) if it's at limit, 
        # 2) if key already exist in list
        # write a function to check for existence and replace if already existed, this should run first as if the key exist then only need to replace and size doesn't matter
        # first add to list if list size is zero, then check for existance and replace, then check for size -> under limit just add, at limit reduce and add

        # if empty list
        if self.size == 0: 
            self.size += 1
            self.storage.add_to_head({key:value})
        
        
        # if existing and replace returns true
        elif self.checkForKeyAndReplace(key, value):
            return

        # else, check for size and proceed with proper addition and removal
        else:
            #if size of list is under limit,    
            if self.size < self.limit:
                self.size += 1
            
            # if size of list if at limit
            else:
                self.storage.remove_from_tail()
            
            self.storage.add_to_head({key:value})


    def checkForKeyAndReplace(self, key, value):
        current = self.storage.head
        if key in current.value:
            current.value[key] = value
            return current

        else:
            while current.next:
                current = current.next
                if key in current.value:
                    current.value[key] = value
                    self.storage.move_to_front(current)
                    return current
  
        return None


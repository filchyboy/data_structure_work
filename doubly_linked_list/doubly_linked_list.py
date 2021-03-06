"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
        
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # prepend
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if not self.head:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        else:
            # if DLL is not empty
            # set new node's next to current head
            new_node.next = self.head
            # set head's prev to new node
            self.head.prev = new_node.next
            # set head to the new node
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        current_head = self.head.value
        self.delete(self.head)
        return current_head

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if not self.head:
            new_node = ListNode(value)
            self.length += 1
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(value)
            self.length += 1
            current_head = self.head
            while current_head.next:
                current_head = current_head.next
            current_head.next = new_node
            new_node.prev = current_head
            new_node.next = None
            self.tail = new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        current_tail = self.tail.value
        self.delete(self.tail)
        return current_tail

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            # self.length -= 1
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current_head = self.head
        while current_head:
            if not current_head.prev:
                if not current_head.next:
                    current_head = None
                    self.head = None
                    self.tail = None
                    self.length -= 1
                    return
                else:
                    next = current_head.next
                    current_head.next = None
                    next.prev = None
                    current_head = None
                    self.head = next
                    self.length -= 1
                    return
            if current_head.next:
                if current_head.prev:
                    next = current_head.next
                    prev = current_head.prev
                    prev.next = next
                    next.prev = prev
                    current_head.next = None
                    current_head.prev = None
                    current_head = None
                    self.length -= 1
                    return
                else:
                    prev = current_head.prev
                    prev.next = None
                    current_head.prev = None
                    current_head = None
                    self.length -= 1
                    return
                    

        
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max = self.head.value
        current_head = self.head
        while current_head: 
            if current_head.value > max:
                max = current_head.next
            current_head = current_head.next
        return max
    
# dllist = DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)
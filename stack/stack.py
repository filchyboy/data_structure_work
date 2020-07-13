from linked_list import Node
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
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return(self.size)

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            self.size += 1
        else:
            new_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node
            self.size += 1

    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            return popped
        


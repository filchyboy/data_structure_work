from linked_list import Node
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
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None
    
    def __len__(self):
        return(self.size)

    def enqueue(self, value):
        if self.last is None:
            self.head = Node(value)
            self.last = self.head
            self.size += 1
        else:
            self.last.next_node = Node(value)
            self.last = self.last.next_node
            self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            return to_return

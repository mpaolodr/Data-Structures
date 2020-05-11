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


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class SinglyLinkedList:
    def __init__(self, node=None):
        self.head = None
        self.tail = None

    def add_to_head(self, data):
        new_node = Node(data)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_head(self):
        if not self.head and not self.tail:
            return
        else:

            value = self.head.data
            self.head = self.head.next
            return value


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = ?

    def __len__(self):
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

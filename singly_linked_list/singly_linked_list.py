class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self, node=None):
        self.head = None
        self.tail = None

    def add_to_head(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            if self.head == self.tail:
                self.head.next = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

    def remove_head(self):

        if not self.head and not self.tail:
            return
        else:
            data = self.head.value

            if self.head == self.tail:
                self.head = None
                self.tail = None
                return data
            else:
                data = self.head.value
                self.head = self.head.next
                return data

    def get_max(self):
        if not self.head and not self.tail:
            return

        if self.head == self.tail:
            return self.head.value

        current = self.head
        value = current.value

        while current.next is not None:
            if current.value > value:
                value = current.value
                current = current.next
            else:
                current = current.next

        if current.value > value:
            value = current.value

        return value

    def contains(self, value):
        if not self.head and not self.tail:
            return False

        if self.head == self.tail:
            if self.head.value == value:
                return True
            else:
                return False

        current = self.head

        while current.next is not None:
            if current.value is value:
                return True
            else:
                current = current.next

        if current.value == value:
            return True

        return False

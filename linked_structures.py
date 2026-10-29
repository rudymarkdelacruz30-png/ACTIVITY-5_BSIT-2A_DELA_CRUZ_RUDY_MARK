class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.top.value

    def __str__(self):
        values = []
        current = self.top
        while current:
            values.append(current.value)
            current = current.next
        return str(values)


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue an empty queue.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.front.value

    def __str__(self):
        values = []
        current = self.front
        while current:
            values.append(current.value)
            current = current.next
        return str(values)

class ArrayStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: stack is full.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop an empty stack.")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.data[self.top]

    def __str__(self):
        return str(self.data[:self.top + 1])


class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: queue is full.")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue an empty queue.")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.data[self.front]

    def __str__(self):
        return str([self.data[(self.front + i) % len(self.data)] for i in range(self.size)])

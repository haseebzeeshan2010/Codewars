class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.front_pos = 0
        self.rear_pos = 0
        self.count = 0 # No. of elements(excluding None) in queue

    def enqueue(self, value):
        self.buffer[self.rear_pos] = value
        self.rear_pos = (self.rear_pos + 1) % self.capacity
        self.count += 1

    def dequeue(self):
        value = self.buffer[self.front_pos]
        self.buffer[self.front_pos] = None
        self.front_pos = (self.front_pos + 1) % self.capacity
        self.count -= 1
        return value

    def is_full(self):
        return self.count == self.capacity

    def is_empty(self):
        return self.count == 0
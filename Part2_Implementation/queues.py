class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.data:
            raise Exception("Queue is empty")
        return self.data.pop(0)

    def peek(self):
        if not self.data:
            raise Exception("Queue is empty")
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)

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

# Creating a queue
queue = Queue()
queue.enqueue(10)  # Enqueue 10
queue.enqueue(20)  # Enqueue 20
queue.enqueue(30)  # Enqueue 30
print("Queue after enqueues:", queue)

print("Dequeued element:", queue.dequeue())  # Dequeue front element
print("Front element:", queue.peek())  # Peek at the front element
print("Is queue empty?", queue.is_empty())

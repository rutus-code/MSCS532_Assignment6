class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.data:
            raise Exception("Stack is empty")
        return self.data.pop()

    def peek(self):
        if not self.data:
            raise Exception("Stack is empty")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)

# Creating a stack
stack = Stack()
stack.push(10)  # Push 10 onto the stack
stack.push(20)  # Push 20
stack.push(30)  # Push 30
print("Stack after pushes:", stack)

print("Popped element:", stack.pop())  # Pop top element
print("Top element:", stack.peek())  # Peek at the top element
print("Is stack empty?", stack.is_empty())

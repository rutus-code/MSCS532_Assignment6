class Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity  # Fixed-size array

    def insert(self, index, value):
        if self.size >= self.capacity:
            raise Exception("Array is full")
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.size - 1] = None
        self.size -= 1

    def access(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def __str__(self):
        return str([self.data[i] for i in range(self.size)])

# Creating an array with capacity 5
array = Array(5)
array.insert(0, 10)  # Insert 10 at index 0
array.insert(1, 20)  # Insert 20 at index 1
array.insert(1, 15)  # Insert 15 at index 1 (shifts others)
print("Array after insertions:", array)

array.delete(1)  # Delete the element at index 1
print("Array after deletion:", array)

print("Access element at index 0:", array.access(0))

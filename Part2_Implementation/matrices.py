class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[None] * cols for _ in range(rows)]

    def insert(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        self.data[row][col] = value

    def access(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bounds")
        return self.data[row][col]

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

# Creating a 3x3 matrix
matrix = Matrix(3, 3)
matrix.insert(0, 0, 1)  # Insert 1 at (0, 0)
matrix.insert(1, 1, 2)  # Insert 2 at (1, 1)
matrix.insert(2, 2, 3)  # Insert 3 at (2, 2)
print("Matrix:")
print(matrix)

print("Access element at (1, 1):", matrix.access(1, 1))

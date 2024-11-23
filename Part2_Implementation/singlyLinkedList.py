class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if not self.head:
            raise Exception("List is empty")
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            raise ValueError("Value not found in the list")

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements

    def __str__(self):
        return " -> ".join(map(str, self.traverse()))

# Creating a singly linked list
linked_list = SinglyLinkedList()
linked_list.insert(10)  # Insert 10
linked_list.insert(20)  # Insert 20
linked_list.insert(30)  # Insert 30
print("Linked list after insertions:", linked_list)

linked_list.delete(20)  # Delete node with value 20
print("Linked list after deletion:", linked_list)

print("Traversal of linked list:", linked_list.traverse())

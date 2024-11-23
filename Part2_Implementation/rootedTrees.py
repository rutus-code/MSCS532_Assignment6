class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __str__(self, level=0):
        result = " " * level + str(self.value) + "\n"
        for child in self.children:
            result += child.__str__(level + 2)
        return result

# Example usage:
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.add_child(child1)
root.add_child(child2)
child1.add_child(TreeNode(4))
child2.add_child(TreeNode(5))
print(root)

# Creating a rooted tree
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)

# Adding children to the root
root.add_child(child1)
root.add_child(child2)

# Adding grandchildren
child1.add_child(TreeNode(4))
child1.add_child(TreeNode(5))
child2.add_child(TreeNode(6))

# Printing the tree
print("Rooted Tree Structure:")
print(root)

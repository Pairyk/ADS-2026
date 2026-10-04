class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, current, value):
        if value > current.data:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insert_recursive(current.right, value)
        elif value < current.data:
            if current.left is None:
                current.left = Node(value)
            else:
                self.insert_recursive(current.left, value)
        
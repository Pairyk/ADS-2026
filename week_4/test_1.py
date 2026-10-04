class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverse_in_order(node):
    if node is None:
        return

    traverse_in_order(node.left)
    print(node.data)
    traverse_in_order(node.right)

def traverse_pre_order(node):
    if node is None:
        return

    print(node.data)
    traverse_pre_order(node.left)
    traverse_pre_order(node.right)

def traverse_post_order(node):
    if node is None:
        return

    traverse_post_order(node.left)
    traverse_post_order(node.right)
    print(node.data)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    traverse_post_order(root)

if __name__ == "__main__":
    main()
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        result = []
        curr = self.tail
        while curr:
            result.append(curr.value)
            curr = curr.prev
        print(*result)

def main():
    _ = input()
    series = map(int, input().split())
    ll = LL()

    for v in series:
        ll.append(v)

    ll.display()

if __name__ == "__main__":
    main()
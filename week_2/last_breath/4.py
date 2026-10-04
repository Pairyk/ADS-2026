class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, v):
        new = Node(v)

        if not self.head:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new

    def display(self):
        result = []
        curr = self.tail
        while curr:
            result.append(curr.val)
            curr = curr.prev
        print(*result)

def main():
    ll = LL()

    stream = input().split()

    for s in stream:
        ll.append(s)

    ll.display()

if __name__ == "__main__":
    main()
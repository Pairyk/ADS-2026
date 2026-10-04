class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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
            self.tail.next = new
            self.tail = new

    def display(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        print(*result)

    def solve(self):
        curr = self.head
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next

def main():
    ll = LL()

    stream = input().split()

    for s in stream:
        ll.append(s)

    ll.solve()
    ll.display()

if __name__ == "__main__":
    main()
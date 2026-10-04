class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        print(*result)

    def delete_duplicate(self):
        curr = self.head
        while curr and curr.next:
            if curr.value == curr.next.value:
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr
            else:
                curr = curr.next

def main():
    amount = int(input())
    ll = LL()

    for _ in range(amount):
        v = input()
        ll.append(v)

    ll.delete_duplicate()
    ll.display()

if __name__ == "__main__":
    main()
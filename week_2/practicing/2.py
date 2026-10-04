class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
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

    def delete_second(self):
        curr = self.head
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next

    def display(self):
        result = []
        curr = self.head
        while curr:
            result.append(str(curr.value))
            curr = curr.next
        print(*result)

def main():
    _ = int(input())
    values = input().split()

    ll = LinkedList()
    for val in values:
        ll.append(val)

    ll.delete_second()

    ll.display()

if __name__ == "__main__":
    main()
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
            return

        self.tail.next = new_node
        self.tail = new_node

    def delete_middle(self, n):
            target_prev_index = (n // 2) - 1
            curr = self.head

            for _ in range(target_prev_index):
                curr = curr.next

            if curr and curr.next:
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr

    def display(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        print(*result)

def main():
    n = int(input())

    if n == 1:
        print("")
        return

    values = input().split()
    ll = LinkedList()

    for val in values:
        ll.append(val)

    ll.delete_middle(n)
    ll.display()

if __name__ == "__main__":
    main()
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

    def delete_duplicate(self):
        current = self.head

        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:  
                current = current.next

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        print(*result)

def main():
    _ = int(input())
    values = input().split()

    ll = LinkedList()
    for val in values:
        ll.append(val)

    ll.delete_duplicate()
    ll.display()

if __name__ == "__main__":
    main()
            
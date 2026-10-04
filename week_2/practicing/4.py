class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
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
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def display_reverse(self):
        result = []
        curr = self.tail
        while curr:
            result.append(curr.value)
            curr = curr.prev
        print(*result)

def main():
    ll = LinkedList()
    values = input().split()
    for val in values:
        ll.append(int(val))
    ll.display_reverse()

if __name__ == "__main__":
    main()
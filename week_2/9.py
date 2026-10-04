class Node:

    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_front(self, title):
        new_node = Node(title)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        print("ok")

    def add_back(self, title):
        new_node = Node(title)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print("ok")

    def erase_front(self):
        if self.size == 0:
            print("error")  #[cite: 7]
            return
        removed_title = self.head.title
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        print(removed_title)

    def erase_back(self):
        if self.size == 0:
            print("error")  #[cite: 7]
            return
        removed_title = self.tail.title
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        print(removed_title)

    def front(self):
        if self.size == 0:
            print("error")  #[cite: 7]
        else:
            print(self.head.title)

    def back(self):
        if self.size == 0:
            print("error")  #[cite: 7]
        else:
            print(self.tail.title)

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("ok")


def solve():
    dll = DoublyLinkedList()

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            parts = line.split(maxsplit=1)
            cmd = parts[0]

            if cmd == "add_front":  #[cite: 7]
                dll.add_front(parts[1])
            elif cmd == "add_back":  #[cite: 7]
                dll.add_back(parts[1])
            elif cmd == "erase_front":  #[cite: 7]
                dll.erase_front()
            elif cmd == "erase_back":  #[cite: 7]
                dll.erase_back()
            elif cmd == "front":  #[cite: 7]
                dll.front()
            elif cmd == "back":  #[cite: 7]
                dll.back()
            elif cmd == "clear":  #[cite: 7]
                dll.clear()
            elif cmd == "exit":  #[cite: 7]
                print("goodbye")  #[cite: 7]
                break
        except EOFError:
            break


if __name__ == "__main__":
    solve()
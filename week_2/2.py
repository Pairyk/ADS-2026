class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def solve():
    # Read input using standard input functions
    n = int(input().strip())
    elements = input().split()

    if n == 0:
        return

    # 1. Build the singly linked list
    head = Node(int(elements[0]))
    current = head
    for val in elements[1:]:
        current.next = Node(int(val))
        current = current.next

    # 2. Delete every second node (even positions)
    current = head
    while current and current.next:
        current.next = current.next.next
        current = current.next

    # 3. Print the remaining values separated by spaces
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next

    print(*result)


if __name__ == "__main__":
    solve()
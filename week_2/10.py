class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, x, p):
    """Command 1: Add a new node with value x at position p."""
    new_node = Node(x)
    if p == 0:
        new_node.next = head
        return new_node

    current = head
    for _ in range(p - 1):
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head


def remove_node(head, p):
    """Command 2: Remove the node at position p."""
    if p == 0:
        return head.next, head.val

    current = head
    for _ in range(p - 1):
        current = current.next

    removed_val = current.next.val
    current.next = current.next.next
    return head, removed_val


def print_list(head):
    """Command 3: Print all values separated by space, or -1 if empty."""
    if not head:
        print("-1")  #[cite: 8]
        return

    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next

    print(" ".join(result))  #[cite: 8]


def replace_node(head, p1, p2):
    """Command 4: Move node from position p1 to position p2."""
    # First remove from p1
    head, val = remove_node(head, p1)
    # Then insert at p2
    head = insert_node(head, val, p2)
    return head


def reverse_list(head):
    """Command 5: Reverse the entire linked list."""
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def get_length(head):
    """Helper function to calculate length of the list."""
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length


def cyclic_left(head, x):
    """Command 6: Make left cyclic shift x times."""
    if not head or x == 0:
        return head

    length = get_length(head)
    x %= length
    if x == 0:
        return head

    # Find the x-th node (new tail) and (x+1)-th node (new head)
    current = head
    for _ in range(x - 1):
        current = current.next

    new_head = current.next
    current.next = None

    # Connect original tail to original head
    tail = new_head
    while tail.next:
        tail = tail.next
    tail.next = head

    return new_head


def cyclic_right(head, x):
    """Command 7: Make right cyclic shift x times."""
    if not head or x == 0:
        return head

    length = get_length(head)
    x %= length
    if x == 0:
        return head

    # A right shift by x is equivalent to a left shift by (length - x)
    return cyclic_left(head, length - x)


def solve():
    head = None

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            parts = list(map(int, line.split()))
            cmd = parts[0]

            if cmd == 0:  #[cite: 8]
                break
            elif cmd == 1:  #[cite: 8]
                x, p = parts[1], parts[2]  #[cite: 8]
                head = insert_node(head, x, p)
            elif cmd == 2:  #[cite: 8]
                p = parts[1]  #[cite: 8]
                head, _ = remove_node(head, p)
            elif cmd == 3:  #[cite: 8]
                print_list(head)
            elif cmd == 4:  #[cite: 8]
                p1, p2 = parts[1], parts[2]  #[cite: 8]
                head = replace_node(head, p1, p2)
            elif cmd == 5:  #[cite: 8]
                head = reverse_list(head)
            elif cmd == 6:  #[cite: 8]
                x = parts[1]  #[cite: 8]
                head = cyclic_left(head, x)
            elif cmd == 7:  #[cite: 8]
                x = parts[1]  #[cite: 8]
                head = cyclic_right(head, x)
        except EOFError:
            break


if __name__ == "__main__":
    solve()
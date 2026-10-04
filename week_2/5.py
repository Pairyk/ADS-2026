class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def solve():
    n = int(input().strip())  #[cite: 3]
    if n == 0:
        return

    elements = input().split()  #[cite: 3]

    # Handle the single node edge case (head is deleted, resulting in an empty list)[cite: 3]
    if n == 1:
        print()  #[cite: 3]
        return

    # 1. Build the singly linked list[cite: 3]
    head = Node(elements[0])
    current = head
    for val in elements[1:]:
        current.next = Node(val)
        current = current.next

    # 2. Find the target index to remove: floor(n / 2)[cite: 3]
    target_idx = n // 2  #[cite: 3]

    # Traverse to the node just before the target node (index target_idx - 1)
    current = head
    for _ in range(target_idx - 1):
        current = current.next

    # Delete the target node by skipping it
    current.next = current.next.next

    # 3. Collect and print remaining nodes[cite: 3]
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next

    print(*result)  #[cite: 3]


if __name__ == "__main__":
    solve()
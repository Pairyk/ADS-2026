class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def solve():
    # Read inputs
    n = int(input().strip())  #[cite: 5]
    elements = list(map(int, input().split()))  #[cite: 5]

    if n == 0:
        return

    # 1. Build the singly linked list
    head = Node(elements[0])
    current = head
    for val in elements[1:]:
        current.next = Node(val)
        current = current.next

    # 2. Traverse the singly linked list and apply Kadane's Algorithm
    # to find the maximum subarray sum (largest run of consecutive days)
    max_sum = head.val
    current_sum = head.val

    current = head.next
    while current:
        # Either extend the existing sequence or start a new sequence from the current node
        current_sum = max(current.val, current_sum + current.val)
        max_sum = max(max_sum, current_sum)
        current = current.next

    # Print the maximum consecutive sum
    print(max_sum)  #[cite: 5]


if __name__ == "__main__":
    solve()
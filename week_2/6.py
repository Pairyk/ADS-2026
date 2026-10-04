class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def build_list(line_tokens):
    """Builds a singly linked list from input line tokens."""
    if not line_tokens:
        return None

    n = int(line_tokens[0])  #[cite: 4]
    if n == 0:  #[cite: 4]
        return None

    # First token after size is the head value
    head = Node(int(line_tokens[1]))  #[cite: 4]
    current = head

    for i in range(2, n + 1):
        current.next = Node(int(line_tokens[i]))  #[cite: 4]
        current = current.next

    return head


def merge_two_lists(l1, l2):
    """Merges two sorted singly linked lists in-place by re-linking next pointers."""
    dummy = Node(0)  # Dummy head to easily manage the head of the merged list
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach the remaining elements if any
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next


def solve():
    # Parse inputs line by line
    line1 = input().split()  #[cite: 4]
    line2 = input().split()  #[cite: 4]

    list1 = build_list(line1)
    list2 = build_list(line2)

    # Merge the two linked lists in-place
    merged_head = merge_two_lists(list1, list2)

    # If both lists were empty, print empty line
    if not merged_head:
        print()  #[cite: 4]
        return

    # Traversal and print
    result = []
    current = merged_head
    while current:
        result.append(str(current.val))
        current = current.next

    print(" ".join(result))  #[cite: 4]


if __name__ == "__main__":
    solve()
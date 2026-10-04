import sys

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    dummy = Node(0)
    curr = dummy
    for val in values:
        curr.next = Node(val)
        curr = curr.next
    return dummy.next

def merge_two_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    p1, p2 = l1, l2
    while p1 and p2:
        if p1.val <= p2.val:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    # Attach the remaining nodes of whichever list is not empty
    tail.next = p1 if p1 else p2

    return dummy.next

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    # Parse first list
    line1 = list(map(int, input_data[0].split()))
    n = line1[0]
    vals1 = line1[1:1 + n]
    
    # Parse second list
    line2 = list(map(int, input_data[1].split()))
    m = line2[0]
    vals2 = line2[1:1 + m]

    list1 = build_list(vals1)
    list2 = build_list(vals2)

    merged_head = merge_two_lists(list1, list2)

    # Collect and print output
    result = []
    curr = merged_head
    while curr:
        result.append(curr.val)
        curr = curr.next

    if result:
        print(*result)
    else:
        print()  # Empty line for empty lists

if __name__ == "__main__":
    solve()



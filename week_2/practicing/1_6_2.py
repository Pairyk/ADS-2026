class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def build_list(vals):
    dummy = Node(0)
    curr = dummy

    for v in vals:
        curr.next = Node(v)
        curr = curr.next

    return dummy.next

def merge_lists(l1, l2):
    dummy = Node(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 if l1 else l2 
    return dummy.next

def main():
    values_1 = list(map(int, input().split()))
    n_1 = values_1[0]
    vals_1 = values_1[1: 1 + n_1]

    values_2 = list(map(int, input().split()))
    n_2 = values_2[0]
    vals_2 = values_2[1: 1 + n_2]


    l1 = build_list(vals_1)
    l2 = build_list(vals_2)

    r1 = merge_lists(l1, l2)

    result = []
    curr = r1
    while curr:
        result.append(curr.val)
        curr = curr.next

    print(*result)


if __name__ == "__main__":
    main()
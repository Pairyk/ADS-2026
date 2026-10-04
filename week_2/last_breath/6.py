class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def builf_list(vals):
    dummy = Node(0)
    curr = dummy
    for val in vals:
        curr.next = Node(val)
        curr = curr.next
    return dummy.next

def merge_lists(l1, l2):
    dummy = Node(0)
    tail = dummy 

    while l1 and l2:
        if l1 <= l2:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
    tail.next = l1 if l1 else l2
    return dummy.next


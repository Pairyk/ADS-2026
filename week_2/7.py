class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

def solve():
    line1 = input().split() 
    if not line1:
        return

    n, k = int(line1[0]), int(line1[1])
    words = input().split()

    if n == 0 or k == 0:
        print(*words)
        return

    head = Node(words[0])
    current = head
    for w in words[1:]:
        current.next = Node(w)
        current = current.next

    tail = current  


    kth_node = head
    for _ in range(k - 1):
        kth_node = kth_node.next
    new_head = kth_node.next
    tail.next = head
    kth_node.next = None

    # 4. Traverse and collect shifted words
    result = []
    current = new_head
    while current:
        result.append(current.val)
        current = current.next

    print(*result)  #[cite: 6]


if __name__ == "__main__":
    solve()
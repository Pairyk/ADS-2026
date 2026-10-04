from bisect import bisect_left, bisect_right

def main():
    _, q = map(int, input().split())
    stream = list(map(int, input().split()))

    def solve(l, r):
        if l > r:
            return 0
        return bisect_right(stream, r) - bisect_left(stream, l)

    result = []
    for _ in range(q):
        l1, r1, l2, r2 = map(int, input().split())
        count = solve(l1, r1) + solve(l2, r2)
        il, ir = max(l1, l2), min(r1, r2)
        count -= solve(il, ir)
        result.append(str(count))

    print(*result)

if __name__ == "__main__":
    main()
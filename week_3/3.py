def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    p = [0] * n
    lol = 0
    for i in range(n):
        lol += a[i]
        p[i] = lol

    answ = []
    for _ in range(m):
        b = int(input())
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if p[mid] >= b:
                right = mid
            else:
                left = mid + 1
        answ.append(str(left + 1))

    print("\n".join(answ))

if __name__ == '__main__':
    main()
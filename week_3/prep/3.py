def main():
    b, m = map(int, input().split())
    stream = list(map(int, input().split()))

    p = [0] * b
    lol = 0
    for i in range(b):
        lol += stream[i]
        p[i] = lol

    result = []

    for _ in range(m):
        ms = int(input())
        left = 0
        right = len(stream) - 1

        while left < right:
            mid = (left+right)//2
            if p[mid] >= ms:
                right = mid
            else:
                left = mid + 1
        result.append(left+1)

    print(*result)


if __name__ == "__main__":
    main()
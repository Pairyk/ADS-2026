def main():
    amn = int(input())
    stream = list(map(int, input().split()))
    target = int(input())
    n = len(stream)

    left, right = 0, n - 1

    while left <= right:
        mid = (left+right)//2
        if stream[mid] == target:
            print("Yes")
            return
        elif stream[mid] < target:
            left = mid + 1
        else:
            right = mid + 1

    print("No")
    return

if __name__ == "__main__":
    main()
def binsearch_upper(a, n, x):
    # returns count of elements <= x (= index where x would go, upper bound)
    left = 0
    right = n - 1
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if a[mid] <= x:
            res = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return res

def main():
    n = int(input())
    a = sorted(map(int, input().split()))

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]


    p = int(input())
    answ = []
    for _ in range(p):
        m = int(input())
        cnt = binsearch_upper(a, n, m)
        answ.append(str(cnt) + " " + str(prefix[cnt]))

    print("\n".join(answ))

if __name__ == '__main__':
    main()

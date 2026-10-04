def main():
    a, n, m = map(int, input().split())

    result = 1 % m
    base = a % m

    while n > 0:
        if n % 2 == 1:
            result = (result * base) % m

        base = (base * base) % m
        n = n // 2

    print(result)

if __name__ == "__main__":
    main()
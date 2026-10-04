def main():
    n = int(input())
    nums = []

    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            nums.append(i)
            n = n // i

    if n > 1:
        nums.append(n)

    print(*nums)

if __name__ == "__main__":
    main()
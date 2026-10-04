def main():
    n = int(input())
    print(Primer(n))


def Primer(n):
    if n <= 1:
        return "NO"

    if n == 2:
        return "YES"

    if n % 2 == 0:
        return "NO"

    for i in range (3, (n**0.5)+1, 2):
        if n % i == 0:
            return "NO"

    return "YES"

if __name__ == "__main__":
    main()
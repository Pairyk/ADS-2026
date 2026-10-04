def main():
    a, b = map(int, input().split())

    while b:
        a, b = b, a%b

    print(a)

if __name__ == "__main__":
    main()
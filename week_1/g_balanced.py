def main():
    s = input()
    arr = []

    for l in s:
        if arr and arr[-1] == l:
            arr.pop()
        else:
            arr.append(l)

    print("NO" if arr else "YES")

if __name__ == "__main__":
    main()

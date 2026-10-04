def solve():
    n = int(input().strip())
    if n == 0:
        print(0)
        return

    # Read the names one by one and keep only non-consecutive duplicates
    unique_names = []
    for _ in range(n):
        name = input().strip()
        if not unique_names or unique_names[-1] != name:
            unique_names.append(name)

    # Print the total count of unique names followed by each name on a new line
    print(len(unique_names))
    for name in unique_names:
        print(name)


if __name__ == "__main__":
    solve()
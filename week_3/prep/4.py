def bin_search(stream, enemies, power):
    left = 0
    right = enemies - 1
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if stream[mid] <= power:
            res = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return res


def main():
    enemies = int(input())
    stream = sorted(map(int, input().split()))
    rounds = int(input())

    # Fix: Size needs to be (enemies + 1) to hold 0 through enemies
    prefix = [0] * (enemies + 1)
    # Fix: Iterating using integer `enemies`
    for i in range(enemies):
        prefix[i + 1] = prefix[i] + stream[i]

    result = []
    for _ in range(rounds):
        power = int(input())
        count = bin_search(stream, enemies, power)
        # Fix: Output both the count and the total power sum
        result.append(f"{count} {prefix[count]}")

    print("\n".join(result))

if __name__ == "__main__":
    main()
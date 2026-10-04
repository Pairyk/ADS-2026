import sys

def main():
    data = sys.stdin.read().split()
    n, h = int(data[0]), int(data[1])
    bags = list(map(int, data[2:2+n]))

    def hours(k):
        return sum((b + k - 1) // k for b in bags)

    lo, hi = 1, max(bags)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    print(lo)

main()
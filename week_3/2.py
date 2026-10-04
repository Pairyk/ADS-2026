import sys
from bisect import bisect_left, bisect_right

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    a = sorted(int(x) for x in data[idx:idx+n]); idx += n

    def count_range(l, r):
        if l > r:
            return 0
        return bisect_right(a, r) - bisect_left(a, l)

    out = []
    for _ in range(q):
        l1, r1, l2, r2 = (int(x) for x in data[idx:idx+4]); idx += 4
        cnt = count_range(l1, r1) + count_range(l2, r2)
        il, ir = max(l1, l2), min(r1, r2)
        cnt -= count_range(il, ir)
        out.append(str(cnt))

    sys.stdout.write("\n".join(out) + "\n")

main()
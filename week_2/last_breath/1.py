from collections import deque, defaultdict

def main():
    series = int(input())

    for _ in range(series):
        _ = input()
        vals = input().split()

        freq = defaultdict(int)
        queue = deque()
        result = []

        for v in vals:
            freq[v] += 1

            if freq[v] == 1:
                queue.append(v)

            while queue and freq[queue[0]] > 1:
                queue.popleft()

            if queue:
                result.append(queue[0])
            else:
                result.append(-1)

        print(*result)                

if __name__ == "__main__":
    main()
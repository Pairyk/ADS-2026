from collections import deque, defaultdict

def main():
    streams = int(input())

    for _ in range(streams):
        _ = input()
        chars = input().split()

        freq = defaultdict(int)
        queue = deque()
        result = []

        for c in chars:
            freq[c] += 1

            if freq[c] == 1:
                queue.append(c)

            while queue and freq[queue[0]] > 1:
                queue.popleft()

            if queue:
                result.append(queue[0])
            else:
                result.append(-1)
            
        print(*result)


if __name__ == "__main__":
    main()
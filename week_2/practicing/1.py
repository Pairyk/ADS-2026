from collections import defaultdict, deque

def main():
    stream = int(input())

    for _ in range(stream):
        freq = defaultdict(int)
        queue = deque()
        result = []

        letters = input().split()

        for l in letters:
            freq[l] += 1

            if freq[l] == 1:
                queue.append(l)

            while queue and freq[queue[0]] > 1:
                queue.popleft()

            if queue:
                result.append(queue[0])
            else:
                result.append(-1)

        print(*result)

if __name__ == "__main__":
    main()
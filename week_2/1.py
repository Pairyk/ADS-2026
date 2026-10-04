from collections import defaultdict, deque

def main():
    streams = int(input())

    for _ in range(streams):
        _ = input()
        letters = input().split()

        freq = defaultdict(int)
        queue = deque()
        result = []

        for char in letters:
            freq[char] += 1

            if freq[char] == 1:
                queue.append(char)

            while queue and freq[queue[0]] > 1:
                queue.popleft()

            if queue:
                result.append(queue[0])
            else:
                result.append("-1")

        print(*result)

if __name__ == "__main__":
    main()
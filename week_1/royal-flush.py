def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        spots = list(range(N))
        deck = [0] * N
        pos = 0
        for k in range(1, N + 1):
            pos = (pos + k) % len(spots)
            deck[spots.pop(pos)] = k
        print(*deck)

if __name__ == '__main__':
    main()
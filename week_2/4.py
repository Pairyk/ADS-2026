import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    n = int(data[0])
    songs = data[1:n+1]
    
    # Reverse and print space-separated
    print(" ".join(songs[::-1]))

if __name__ == "__main__":
    main()
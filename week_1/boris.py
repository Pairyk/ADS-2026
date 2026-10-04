from collections import deque

def solve():
    boris = deque(map(int, input().split()))
    nursik = deque(map(int, input().split()))
    
    moves = 0
    
    while boris and nursik:
        b_card = boris.popleft()
        n_card = nursik.popleft()
        
        if (b_card == 0 and n_card == 9):
            boris_wins = True
        elif (b_card == 9 and n_card == 0):
            boris_wins = False
        else:
            boris_wins = b_card > n_card
            
        if boris_wins:
            boris.append(b_card)
            boris.append(n_card)
        else:
            nursik.append(b_card)
            nursik.append(n_card)
            
        moves += 1
        
    if boris:
        print(f"Boris {moves}")
    else:
        print(f"Nursik {moves}")

if __name__ == '__main__':
    solve()
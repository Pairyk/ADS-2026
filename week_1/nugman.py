def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    stack = []
    result = []
    
    for val in a:
        while stack and stack[-1] >= val:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
            
        stack.append(val)
        
    print(*result)

if __name__ == '__main__':
    solve()
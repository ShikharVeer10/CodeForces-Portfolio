def solve():
    t = int(input())  
    for _ in range(t):
        n, k = map(int, input().split())
        

        possible = False
        for y in range(n // k + 1):
            if (n - k * y) % 2 == 0:
                possible = True
                break
        
        if possible:
            print("YES")
        else:
            print("NO")


solve()

t=int(input())

for _ in range(t):
    n=int(input())
    
    if n%2020<=n//2020:
        print("Yes")
    else:
        print("No")

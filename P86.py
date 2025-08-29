t=int(input())

for _ in range(t):
    n,m,p,q=map(int,input().split())
    if m*p==(n-p+1)*q:
        print("YES")
    else:
        print("NO")
    
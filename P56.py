t=int(input())

for _ in range(t):
    a,b,c=map(int,input().split())
    total=a+b+c
    if total%3==0:
        target=total//3
        if c>=target:
            print("YES")
        else:
            print("NO")
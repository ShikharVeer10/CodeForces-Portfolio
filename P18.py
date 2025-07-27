n=int(input())
for _ in range(n):
    a,b,c,n=map(int,input().split())
    
    total=a+b+c+n
    max_coins=max(a,b,c)
    equal=total//3
    
    if total%3==0 and max_coins<=equal:
        print("YES")
    else:
        print("NO")
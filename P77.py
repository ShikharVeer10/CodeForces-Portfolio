t=int(input())

for _ in range(t):
    l,r,a=map(int,input().split())
    
    ans=(r//a)+(r%a)
    
    x2=(r//a)*a-1
    if x2>=l:
        ans=max(ans,(x2//a)+(x2%a))
        
    
    print(ans)
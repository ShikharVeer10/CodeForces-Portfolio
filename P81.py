t=int(input())

for _ in range(t):
    n=int(input())
    max_quality=-1
    winner_index=-1
    
    for i in range(1,n+1):
        a,b=map(int,input().split())
        if a<=10 and b>max_quality:
            max_quality=b
            winner_index=i
    print(winner_index) 
    
    
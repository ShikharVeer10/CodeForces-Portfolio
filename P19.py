t=int(input())

for _ in range(t):
    a,b=map(int,input().split())
    diff=b-a
    
    if diff==0:
        print(0)
    elif diff>0:
        print(1 if diff % 2 == 1 else 2) 
    else:
        print(1 if diff % 2 == 0 else 2)

import math

def min_moves(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 2
    elif n%2==0:
        return 2
    else:
        is_prime=True
        for d in range(2,int(math.isqrt(n))+1):
            if n%d==0:
                is_prime=False
                break
        if is_prime:
            return 3
        else:
            return 3
    
t=int(input())

for _ in range(t):
    n=int(input())
    print(min_moves(n))
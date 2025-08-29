import math

def find_a_b(s):
    num=int(s)
    max_sum=int(math.isqrt(num))+1
    for a in range(0,max_sum+1):
        remaining=num-a*a
        if remaining<0:
            continue
        b=int(math.isqrt(remaining))
        if b*b==remaining and (a+b)**2==num:
            return (a,b)
    return -1

t=int(input())
for _ in range(t):
    s=input().strip()
    result=find_a_b(s)
    if result==-1:
        print(-1)
    else:
        a,b=result
        print(a,b)
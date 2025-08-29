t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    max_sum=max(a)
    print(2*max_sum-total)
t=int(input())

for _ in range(t):
    b,c,h=map(int,input().split())
    fillings=min(c+h,b-1)
    print(2*fillings+1)
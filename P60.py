t=int(input())

for _ in range(t):
    a,b,c=map(int,input().split())
    y = c + 1
    z = y * (a + 1) + b
    x = z * (b + 1) + a
    print(x,y,z)
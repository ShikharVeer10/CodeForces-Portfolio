n=int(input())

a=list(map(int,input().split()))

a.sort()
found=False
for i in range(n-2):
    if a[i]+a[i+1]>a[i+2]:
        found=True
        break
    

print("Yes" if found else "No")
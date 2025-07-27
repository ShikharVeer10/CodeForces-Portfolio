t = int(input())  
base = "Yes" * 100  

for _ in range(t):
    s = input().strip()
    if s in base:
        print("YES")
    else:
        print("NO")

t=int(input())

for _ in range(t):
    a, b = input().split()
    
    if(a==b):
        print("=")
        continue
    
    if a=="M":
        print(">" if b[-1] == "S" else "<")
        continue
    if b == "M":
        print("<" if a[-1] == "S" else ">")
        continue

    if a[-1] == "S" and b[-1] == "S":
        print("<" if len(a) > len(b) else ">")
        continue

    if a[-1] == "L" and b[-1] == "L":
        print(">" if len(a) > len(b) else "<")
        continue
    print("<" if a[-1] == "S" else ">")
        
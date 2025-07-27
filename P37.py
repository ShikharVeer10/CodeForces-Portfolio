t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ones = a.count(1)
    twos = a.count(2)
    total = sum(a)

    if total % 2 != 0:
        print("NO")
    elif ones == 0 and twos % 2 != 0:
        print("NO")
    else:
        print("YES")

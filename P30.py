
t = int(input())
for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    occupied = set()

    occupied.add(a[0])
    valid = True

    for i in range(1, n):
        seat = a[i]
       
        if seat - 1 not in occupied and seat + 1 not in occupied:
            valid = False
            break

        occupied.add(seat)
    if valid:
        print("YES")
    else:
        print("NO")

# Read input
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


set_A = set(A)
set_B = set(B)

for a in A:
    for b in B:
        if (a + b) not in set_A and (a + b) not in set_B:
            print(a, b)
            exit()

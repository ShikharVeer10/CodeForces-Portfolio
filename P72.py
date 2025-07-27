import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, j, k = map(int, input[ptr:ptr+3])
        ptr +=3
        a = list(map(int, input[ptr:ptr+n]))
        ptr +=n
        j_strength = a[j-1]
        sorted_a = sorted(a)
        if j_strength >= sorted_a[n -k]:
            print("YES")
        else:
            print("NO")

solve()
n = int(input())
f = list(map(int, input().split()))

# Convert to 0-based index to simplify indexing
f = [x - 1 for x in f]

for i in range(n):
    a = f[i]
    b = f[a]
    c = f[b]
    if c == i:
        print("YES")
        break
else:
    print("NO")
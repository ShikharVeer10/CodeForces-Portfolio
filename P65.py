t = int(input())
mirror = {'p': 'q', 'q': 'p', 'w': 'w'}

for _ in range(t):
    a = input()
    b = ''.join(mirror[c] for c in reversed(a))
    print(b)

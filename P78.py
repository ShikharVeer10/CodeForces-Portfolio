t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    found = False

    if (2 * b - c) % a == 0 and (2 * b - c) // a >= 1:
        found = True

    elif (a + c) % (2 * b) == 0 and (a + c) // (2 * b) >= 1:
        found = True

    elif (2 * b - a) % c == 0 and (2 * b - a) // c >= 1:
        found = True

    print("YES" if found else "NO")

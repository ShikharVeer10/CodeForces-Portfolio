t=int(input())

for _ in range(t):
    s=input()
    keys_collected=set()
    possible=True
    for ch in s:
        if ch.islower():
            keys_collected.add(ch)
        else:
            if ch.lower() not in keys_collected:
                possible=False
                break
    print("YES" if possible else "NO")
            
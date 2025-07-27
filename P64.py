t=int(input())

for _ in range(t):
    n=list(map(int,input().split()))
    
    d = d.strip()
    s = input().strip()
    inserted = False
    res = []

    for ch in s:
        if not inserted and d > ch:
            res.append(d)
            inserted = True
        res.append(ch)
    
    if not inserted:
        res.append(d)

    print(''.join(res))
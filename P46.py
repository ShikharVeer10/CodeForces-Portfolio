t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    completed_tasks = set()
    prev_task = s[0]
    suspicious = False
    
    for i in range(1, n):
        if s[i] != prev_task:
            completed_tasks.add(prev_task)
            if s[i] in completed_tasks:
                suspicious = True
                break
            prev_task = s[i]
    
    print("NO" if suspicious else "YES")

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]==a[1]:
        all_same= True
        for num in a:
            if num != a[0]:
                all_same = False
                break
        if all_same:
            print("NO")
        else:
            found = False
            for i in range(1, n):
                if a[i] != a[0]:
                    a[0], a[i] = a[i], a[0]
                    found = True
                    break
            if found:
                print("YES")
                print(' '.join(map(str, a)))
            else:
                print("NO")
    else:
        print("YES")
        print(' '.join(map(str, a)))
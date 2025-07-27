n=int(input())
arr=list(map(int,input().split()))

unique_sorted=sorted(set(arr))
if len(unique_sorted)>=2:
    print(unique_sorted[1])
else:
    print("NO")
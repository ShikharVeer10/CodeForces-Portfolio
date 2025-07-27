def count_valid_pairs(n,m):
    count=0
    for a in range(n+1):
        for b in range(m+1):
            if a**2+b==n and a+b**2==m:
                count+=1
    return count
        
n,m=map(int,input().split())
print(count_valid_pairs(n,m))

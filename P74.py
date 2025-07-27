t=int(input())

for _ in range(t):
    n=int(input())
    total_count=[0]*26
    
    for _ in range(n):
        s=input().strip()
        for ch in s:
            total_count[ord(ch) - ord('a')] +=1
            
    possible=all(count %n==0 for count in total_count)
    print("YES" if possible else "NO")
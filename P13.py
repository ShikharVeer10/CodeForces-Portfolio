n=int(input())
s=input()
removal_count=0
for i in range(n-1):
    if s[i] == s[i+1]:
        removal_count += 1
         
print(removal_count)

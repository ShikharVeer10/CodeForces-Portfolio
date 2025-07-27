n=int(input())
s=input()

groups=[]
count=0

for char in s:
    if char =='B':
        count+=1
    else:
        if count>0:
            groups.append(count)
            count=0
            
if count > 0:
    groups.append(count)
print(len(groups))
if groups:
    print(' '.join(map(str, groups)))
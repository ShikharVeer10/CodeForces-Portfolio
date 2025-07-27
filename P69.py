n=int(input())

feeling=[]

for i in range(1,n+1):
    if i%2==1:
        feeling.append("I hate ")
    else:
        feeling.append("I love ")
    if i!=n:
        feeling.append("that ")

feeling.append("it ")

print(''.join(feeling))
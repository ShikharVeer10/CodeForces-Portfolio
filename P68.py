n=int(input())
a=int(input())
b=int(input())
c=int(input())

total_distance=0

if n==1:
    print(0)
else:
    total_distance+=min(a,b)
    remaining_meals=n-2
    if remaining_meals>=0:
        total_distance += remaining_meals * min(a, b, c)
    print(total_distance)
n=int(input())

solved_count=0
for _ in range(n):  
    petya, vasya, tonya = map(int, input().split())
    if petya + vasya + tonya >= 2:
        solved_count += 1
print(solved_count)
t = int(input().strip())  
correct = sorted("Timur")  

for _ in range(t):
    n = int(input().strip()) 
    s = input().strip()  
    if n == 5 and sorted(s) == correct:
        print("YES")
    else:
        print("NO")

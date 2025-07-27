t=int(input("Enter the number of testcases: "))
results=[]
for _ in range(t):
    a,b,c=map(int,input().split())
    
    if a+b==c:
        results.append("+")
    else:
        results.append("-")
        
    print("\n".join(results)) 
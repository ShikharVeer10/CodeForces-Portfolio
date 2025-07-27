def minimum_moves():
    t=int(input("Enter the number of test cases: "))
    results=[]
    
    for _ in range(t):
        a,b = map(int, input().split())
        
        if a==b:
            results.append(0)
        elif a<b:
            if(a%2) == (b%2):
                results.append(1)
            else:
                results.append(2)
        else:
            if (a%2) == (b%2):
                results.append(1)
            else:
                results.append(2)
        print("\n".join(map(str, results)))
        
        
minimum_moves()
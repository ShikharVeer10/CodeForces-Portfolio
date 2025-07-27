#Construct a Rectangle
def can_form_rectangle(l1,l2,l3):
    if (l1==l2 and l3%2==0) or (l1==l3 or l2%2==0) or (l2==l3 or l1%2==0):
        return True
    elif l1+l2==l3 or l2+l3==l1 or l1+l3==l2:
        return True
    return False

t=int(input())

for _ in range(t):
    l1,l2,l3=map(int,input().split())
    print("YES" if can_form_rectangle(l1, l2, l3) else "NO")
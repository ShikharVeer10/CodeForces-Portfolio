def can_divide_watermelon():
    if w>2 and w%2==0:
        return "YES"
    else:
        return "NO"

w=int(input("Enter the value: "))
print(can_divide_watermelon())
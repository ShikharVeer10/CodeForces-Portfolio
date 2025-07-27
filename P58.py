def is_interesting(n):
    return sum(int(digit) for digit in str(n)) % 4 == 0

a = int(input())

while not is_interesting(a):
    a += 1

print(a)

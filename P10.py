n = int(input())  
previous_magnet = ""
groups = 0

for _ in range(n):
    current_magnet = input().strip()
    if current_magnet != previous_magnet:  
        groups += 1
    previous_magnet = current_magnet
    
print(groups)

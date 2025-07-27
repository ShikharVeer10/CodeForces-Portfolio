k,n,s,p=map(int,input().split())

sheets_per_person=(n+s-1)//s
total_sheets=sheets_per_person*k
packs_needed = (total_sheets + p - 1) // p
print(packs_needed)
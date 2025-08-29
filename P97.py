n,m,a=map(int,input().split())

tiles_along_n=(n+a-1)//a
tiles_along_m=(m+a-a)//a

total_tiles=tiles_along_m*tiles_along_n
print(total_tiles)
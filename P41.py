l,r,a=map(int,input().split())

if l<r:
  diff=min(r-l,a)
  l+=diff
  a-=diff
  
elif r<l:
    diff=min(l-r,a)
    r+=diff
    a-=diff

equal=a//2
team_size = (l + equal) * 2

max_size=min((l+r+a)//2,min(l+a,r+a))
team_s=max_size*2
print(team_s)
print(team_size)  
    
n,k=map(int,input().split())
y=list(map(int,input().split()))

eligible=[yi for yi in y if yi <=5-k]

print(len(eligible)//3)
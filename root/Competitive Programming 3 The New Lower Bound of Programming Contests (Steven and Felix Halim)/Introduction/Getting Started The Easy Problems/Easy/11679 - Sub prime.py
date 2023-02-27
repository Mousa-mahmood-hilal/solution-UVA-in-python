# user: Mousa-mahmood-hilal
#Problem: UVA 11679 - Sub-prime
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    b=list(map(int,input().split()))
    for i in range(m):
        x,y,z=map(int,input().split())
        b[y-1]+=z
        b[x-1]-=z
    f=False
    for i in b:
        if i<0:
            f=True
            break
    if f:
        print('N')
    else:
        print('S')
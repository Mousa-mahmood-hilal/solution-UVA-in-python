# user: Mousa-mahmood-hilal
#Problem: UVA 10919 - Prerequisites?
while True:
    tem=list(map(int,input().split()))
    k=tem[0]
    if not k:
        break
    m=tem[1]
    f=True
    d={}
    te=list(map(str,input().split()))
    for i in range(k):
        d[te[i]]=1
    for j in range(m):
        t=list(map(str,input().split()))
        c=int(t[0])
        r=int(t[1])
        for i in range(c):
            if t[i+2]   in d.keys():
                r-=1
        if r>0:
            f=False
    if f:
        print('yes')
    else:
        print('no')
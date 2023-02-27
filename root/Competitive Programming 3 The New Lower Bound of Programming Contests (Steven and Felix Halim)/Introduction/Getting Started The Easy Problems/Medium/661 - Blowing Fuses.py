# user: Mousa-mahmood-hilal
#Problem: UVA 661 - Blowing Fuses
Sequence=1
while True:
    n,m,c=map(int,input().split())
    if n==0 and m==0 and c==0:
        break
    print('Sequence '+str(Sequence))
    Sequence+=1
    t=[]
    d={}
    for i in range(n):
        t.append(int(input()))
    s=0;mx=0
    for i in range(m):
        k=int(input())
        if k not in d.keys():
            d[k]=True
            s+=t[k-1]
        else:
            d[k]=False
            del d[k]
            s-=t[k-1]
        mx=max(s,mx)
    if mx<=c:
        print('Fuse was not blown.')
        print('Maximal power consumption was '+ str(mx) +' amperes.')
    else:
        print('Fuse was blown.')
    print()
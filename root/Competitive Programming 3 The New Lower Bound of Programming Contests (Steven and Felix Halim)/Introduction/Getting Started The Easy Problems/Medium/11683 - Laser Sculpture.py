# user: Mousa-mahmood-hilal
#Problem: UVA 11683 - Laser Sculpture
while True:
    a=list(map(int,input().split()))
    A=a[0]
    if not A:
        break
    C=a[1]
    l=list(map(int,input().split()))
    lh=A;ans=0
    for i in range(C):
        if lh>l[i]:
            ans+=lh-l[i]
        lh=l[i]
    print(ans)
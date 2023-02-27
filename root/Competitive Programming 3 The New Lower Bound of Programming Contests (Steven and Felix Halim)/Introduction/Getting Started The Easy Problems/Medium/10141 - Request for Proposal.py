# user: Mousa-mahmood-hilal
#Problem: UVA 10141 - Request for Proposal
c=0
while True:
    n,p=map(int,input().split())
    if not n and not p:
        break
    c+=1
    price = 2000000000.00
    rm=-1
    name=''
    for i in range(n):
        s=input()
    while p:
        s=input()
        a=list(map(float,input().split()))
        p1=a[0]
        rm1=int(a[1])
        if rm1>rm:
            rm=rm1
            name=s
            price=p1
        elif rm1==rm and p1<price:
            rm=rm1
            name=s
            price=p1
        for i in range(rm1):
            s=input()
        p-=1
    if c>1:
        print()
    print('RFP #'+ str(c))
    print(name)
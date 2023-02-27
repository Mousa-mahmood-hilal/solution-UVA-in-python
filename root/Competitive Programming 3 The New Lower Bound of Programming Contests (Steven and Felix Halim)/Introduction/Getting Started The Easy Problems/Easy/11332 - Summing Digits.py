# user: Mousa-mahmood-hilal
#Problem: UVA 11332 - Summing Digits
while True:
    n=list(map(int,input()))
    if n[0]==0:
        break
    a=[]
    s=str(sum(n))
    while len(s)!=1:
        t=0
        for i in s:
            t+=int(i)
        s=str(t)
    print(s)
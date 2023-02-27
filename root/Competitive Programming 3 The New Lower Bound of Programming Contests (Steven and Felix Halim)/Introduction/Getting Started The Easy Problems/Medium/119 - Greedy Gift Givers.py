# user: Mousa-mahmood-hilal
#Problem: UVA 119 - Greedy Gift Givers
k=1
while True:
    try:
        n=int(input())
        t=list(input().split())
        d={}
        for i in t:
            d[i]=0
        for i in range(n):
            t=list(input().split())
            c=int(t[1])
            np=int(t[2])
            if np==0:
                continue
            g=c//np
            d[t[0]]-=g*np
            for j in range(np):
                d[t[j+3]]+=g
        # for print line between cases
        if k>1:
            print()
        for keys, value in d.items():
            f=True
            print(str(keys)+' '+str(value))
        k+=1
        d.clear()
    except:
        break
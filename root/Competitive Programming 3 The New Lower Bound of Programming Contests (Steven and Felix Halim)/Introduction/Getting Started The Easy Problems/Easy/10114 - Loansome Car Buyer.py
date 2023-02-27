# user: Mousa-mahmood-hilal
#Problem: UVA 10114 - Loansome Car Buyer
while True:
    arr1=list(map(float,input().split()))
    d=int(arr1[0]);dp=arr1[1];l=arr1[2];nr=int(arr1[3])
    if d<0:
        break
    vc=l+dp
    mp=l/d
    dl=[]
    dv=[]
    arr1.clear()
    for i in range(nr):
        arr1=list(map(float,input().split()))
        dl.append(int(arr1[0]))
        dv.append(arr1[1])
    lm=0
    lv=dv[0]
    vc*=(1-lv)
    if l<vc:
        print('0 months')
        continue
    lm=1
    for i in range(1,len(dl)):
        nm=dl[i]
        nmd=dv[i]
        while lm<=nm:
            if nm==lm:
                lv=nmd
            vc*=(1-lv)
            l-=mp
            lm+=1
            if l<vc:
                break
        if l<vc:
            break
    while l>vc:
        vc*=(1-lv)
        l-=mp
        lm+=1
    lm-=1
    if lm ==1:
        print('1 month')
    else:
        print(str(lm)+' months')
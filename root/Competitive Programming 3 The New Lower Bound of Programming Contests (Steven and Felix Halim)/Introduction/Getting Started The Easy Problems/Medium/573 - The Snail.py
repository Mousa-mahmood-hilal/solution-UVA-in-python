# user: Mousa-mahmood-hilal
#Problem: UVA 573 - The Snail 
while True:
    h,u,d,f=map(float,input().split())
    if not h:
        break
    ans=0.0
    day=0
    f=u*(f/100.00)
    while True:
        day+=1
        ans+=u      
        if ans>h:
            print('success on day '+str(day))
            break
        ans-=d
        if ans<0:
            print('failure on day '+str(day))
            break
        u-=f
        if u<0:
            u=0
# user: Mousa-mahmood-hilal
#Problem: UVA 11723 - Numbering Roads
i=0
while True:
    r,n=map(int,input().split())
    if r==0 and n==0:
        break
    x=r//n
    if r%n==0:
        x-=1
    if x>26:
        print('Case '+str(i+1)+': impossible')
    else:
        print('Case '+str(i+1)+': '+str(x))
    i+=1
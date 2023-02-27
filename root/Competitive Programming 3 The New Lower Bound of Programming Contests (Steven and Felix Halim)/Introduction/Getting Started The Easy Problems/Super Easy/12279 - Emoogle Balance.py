# user: Mousa-mahmood-hilal
#Problem: 12279 - Emoogle Balance
i=0
while True:
    n= int(input())
    if not n:
        break
    arr=list(map(int,input().split()))
    r=arr.count(False)
    print('Case '+str(i+1)+': '+str(len(arr)-r*2))
    i+=1
# user: Mousa-mahmood-hilal
#Problem: UVA 11559 - Event Planning
while True:
    try:
        n,b,h,w=map(int,input().split())
        mc=b+1
        for i in range (h):
            p=int(input())
            arr=list(map(int,input().split()))
            for j in arr:
                if j>=n and p*n<=mc:
                    mc=p*n
        if mc<=b:
            print(mc)
        else:
            print('stay home')
    except:
        break
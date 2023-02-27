# user: Mousa-mahmood-hilal
#Problem: UVA 11764 - Jumping Mario
test_cases=int(input())
for j in range(test_cases):
    n=int(input())
    arr=list(map(int,input().split()))
    hj=0
    lj=0
    for i in range (1,n):
        if arr[i]<arr[i-1]:
            lj+=1
        elif arr[i]>arr[i-1]:
            hj+=1
    print('Case '+str(j+1)+': '+str(hj)+' '+str(lj))
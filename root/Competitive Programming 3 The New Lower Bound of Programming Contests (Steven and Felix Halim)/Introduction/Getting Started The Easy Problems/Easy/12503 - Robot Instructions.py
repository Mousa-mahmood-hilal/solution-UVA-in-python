# user: Mousa-mahmood-hilal
#Problem: UVA 	12503 - Robot Instructions
test_cases=int(input())
while test_cases:
    n=int(input())
    arr=[]
    ans=0
    for i in range(n):
        t=list(map(str,input().split()))
        if len(t)>1:
            arr.append(arr[int(t[2])-1])
        else:
            arr.append(t[0])
        if arr[i]=='LEFT':
            ans-=1
        else:
            ans+=1
    print(ans)
    test_cases-=1
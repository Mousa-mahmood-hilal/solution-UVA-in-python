# user: Mousa-mahmood-hilal
#Problem: 11364 - Parking
test_cases=int(input())
while test_cases:
    n=int(input())
    arr=list(map(int,input().split()))
    s=0
    arr.sort()
    for i in range(1,n):
        s+=(arr[i]-arr[i-1])
    s+=arr[n-1]-arr[0]
    print(s)
    test_cases-=1
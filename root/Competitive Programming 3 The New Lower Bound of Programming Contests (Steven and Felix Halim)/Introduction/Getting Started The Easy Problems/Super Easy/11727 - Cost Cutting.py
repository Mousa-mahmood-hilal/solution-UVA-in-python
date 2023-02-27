# user: Mousa-mahmood-hilal
#Problem: 11727 - Cost Cutting
test_case=int(input())
for i in range(test_case):
    arr=list(map(int,input().split()))
    arr.sort()
    print('Case '+str(i+1)+': '+str(arr[1]))
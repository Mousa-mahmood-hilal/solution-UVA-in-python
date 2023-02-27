# user: Mousa-mahmood-hilal
#Problem: 12403 - Save Setu
test_cases=int(input())
sum=0
while test_cases:
    arr=list(input().split())
    if len(arr)==2:
        sum+=int(arr[1])
    else:
        print(sum)
    test_cases-=1
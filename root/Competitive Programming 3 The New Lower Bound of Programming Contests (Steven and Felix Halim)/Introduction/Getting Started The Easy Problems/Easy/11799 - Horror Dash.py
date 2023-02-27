# user: Mousa-mahmood-hilal
#Problem: UVA 11799 - Horror Dash
test_cases=int(input())
for i in range(test_cases):
    arr=list(map(int,input().split()))
    print('Case '+str(i+1)+': '+str(max(arr)))
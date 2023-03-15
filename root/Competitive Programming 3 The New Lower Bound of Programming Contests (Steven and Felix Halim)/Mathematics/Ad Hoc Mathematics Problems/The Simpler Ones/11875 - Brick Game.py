# user: Mousa-mahmood-hilal
#Problem: UVA 11875 - Brick Game
test_cases=int(input())
for i in range(test_cases):
    arr=[*map(int,input().split())]
    print('Case '+str(i+1)+': '+str(arr[arr[0]//2+1]))
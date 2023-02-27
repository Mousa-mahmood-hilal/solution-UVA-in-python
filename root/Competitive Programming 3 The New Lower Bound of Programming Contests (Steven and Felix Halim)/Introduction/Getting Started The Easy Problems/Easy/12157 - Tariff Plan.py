# user: Mousa-mahmood-hilal
#Problem: UVA 	12157 - Tariff Plan
test_cases =int(input())
for i in range (test_cases):
    n=int(input())
    arr=list(map(int,input().split()))
    mileCost=0
    juiceCost=0
    for k in arr:
        mileCost += (k // 30) * 10 + 10
        juiceCost += (k // 60) * 15 + 15
    if mileCost<juiceCost:
        print('Case '+str(i+1)+': '+'Mile '+str(mileCost))
    elif juiceCost<mileCost:
        print('Case '+str(i+1)+': '+'Juice '+str(juiceCost))
    else:
        print('Case '+str(i+1)+': '+'Mile Juice '+str(mileCost))
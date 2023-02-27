# user: Mousa-mahmood-hilal
#Problem: 12372 - Packing for Holiday
test_cases=int(input())
for i in range(test_cases):
    L,W,H=map(int,input().split())
    if L<=20 and W<=20 and H<=20:
        print('Case '+str(i+1)+': '+'good')
    else:
        print('Case '+str(i+1)+': '+'bad')

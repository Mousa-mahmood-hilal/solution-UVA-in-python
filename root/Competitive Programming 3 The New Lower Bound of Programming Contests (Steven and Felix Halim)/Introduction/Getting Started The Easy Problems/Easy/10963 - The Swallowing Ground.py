# user: Mousa-mahmood-hilal
#Problem: UVA 10963 - The Swallowing Ground
test_cases=int(input())
while test_cases:
    input()
    n=int(input())
    u,d=map(int,input().split())
    f=False
    res=u-d
    for i in range(n-1):
        u,d=map(int,input().split())
        if res!=u-d:
            f=True
    if not f:
        print('yes')
    else:
        print('no')
    if test_cases-1:
        print()
    test_cases-=1
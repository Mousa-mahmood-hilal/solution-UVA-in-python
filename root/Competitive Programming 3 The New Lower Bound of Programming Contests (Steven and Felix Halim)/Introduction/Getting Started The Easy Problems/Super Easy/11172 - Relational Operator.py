# user: Mousa-mahmood-hilal
#Problem: 11172 - Relational Operator
test_cases=int(input())
while test_cases:
    n,m=map(int,input().split())
    if n>m:
        print('>')
    elif n<m:
        print('<')
    else:
        print('=')
    test_cases-=1
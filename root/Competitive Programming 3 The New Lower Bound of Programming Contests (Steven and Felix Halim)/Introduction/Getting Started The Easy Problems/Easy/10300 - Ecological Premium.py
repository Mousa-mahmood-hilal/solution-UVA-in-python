# user: Mousa-mahmood-hilal
#Problem: UVA 10300 - Ecological Premium
test_cases=int(input())
while test_cases:
    n=int (input())
    s=0
    for i in range(n):
        a,b,c=map(int,input().split())
        s+=a*c
    print(s)
    test_cases-=1
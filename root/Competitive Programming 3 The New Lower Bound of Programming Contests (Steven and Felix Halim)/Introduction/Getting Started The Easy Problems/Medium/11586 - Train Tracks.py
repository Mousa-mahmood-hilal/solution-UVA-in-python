# user: Mousa-mahmood-hilal
#Problem: UVA 11586 - Train Tracks
test_cases=int(input())
while test_cases:
    l=list(map(str,input().split()))
    s=''.join(l)
    m=s.count('M')
    f=s.count('F')
    if m==f:
        print('LOOP')
    else:
        print('NO LOOP')
    test_cases-=1
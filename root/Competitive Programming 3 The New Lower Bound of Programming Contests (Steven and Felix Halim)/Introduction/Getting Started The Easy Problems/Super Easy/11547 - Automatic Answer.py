# user: Mousa-mahmood-hilal
#Problem: 11547 - Automatic Answer
test_cases=int(input())
while test_cases:
    n=int(input())
    s=str((((n*63)+7492)*5)-498)
    
    print(s[len(s)-2])
    test_cases-=1
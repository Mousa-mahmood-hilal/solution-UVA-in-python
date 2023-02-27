# user: Mousa-mahmood-hilal
#Problem: 12289 - One-Two-Three
test_cases=int(input())
while test_cases:
    s=input()
    one='one'
    two='two'
    three='three'
    if len(s)==3:
        f=0;se=0
        for i  in range(3):
            if s[i]   in one:
                f+=1
                one=one.replace(s[i],'&',1)
        if f>1:
            print(1)
        else:
            print(2)
    else:
        print(3)
    test_cases-=1
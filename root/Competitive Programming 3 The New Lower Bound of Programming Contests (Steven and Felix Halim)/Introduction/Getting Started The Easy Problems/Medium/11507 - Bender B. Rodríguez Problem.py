# user: Mousa-mahmood-hilal
#Problem: UVA 11507 - Bender B. Rodríguez Problem
while True:
    l=int(input())
    if not l:
        break
    l-=1
    sighn=1
    ch='x'
    f=False
    s=list(map(str,input().split()))
    for i in range(l):
        f=False
        if 'No' == s[i]:
            continue
        ss=s[i]
        if ch =='x' and ss[0] == '-':
            f=True
        if ch =='y' and ss=='+y':
            f=True
        if ch =='z' and ss=='+z':
            f=True
        if f:
            sighn*=-1
        if ch == 'x' :
            ch = ss[1]
        elif ch == 'y' and  'y' in ss :
            ch = 'x'
        elif ch == 'z' and 'z' in ss: 
            ch = 'x'
    if sighn>0:
        print('+' + str(ch))
    else:
        print('-' + str(ch))
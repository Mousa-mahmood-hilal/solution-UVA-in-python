# user: Mousa-mahmood-hilal
#Problem: UVA 11661 - Burger Time?
while True:
    L=int(input())
    if not L:
        break
    s=input()
    r=-L;d=-L
    if 'Z' in s:
        print(0)
        continue
    mn=L
    for i in range(L):
        if s[i] =='R':
            mn=min(mn,i-d)
            r=i
        elif s[i]=='D':
            mn=min(mn,i-r)
            d=i           
    print(mn)
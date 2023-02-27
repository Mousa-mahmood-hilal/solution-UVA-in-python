# user: Mousa-mahmood-hilal
#Problem: UVA 12015 - Google is Feeling Lucky
test_cases=int(input())
for i in range(test_cases):
    mxn=0
    mxs=[]
    for j in range(10):
        s,n=input().split()
        if mxn<int(n):
            mxn=int(n)
            mxs.clear()
            mxs.append(s)
        elif mxn==int(n):
            mxs.append(s)
    print('Case #'+str(i+1)+':\n' + '\n'.join(mxs))   
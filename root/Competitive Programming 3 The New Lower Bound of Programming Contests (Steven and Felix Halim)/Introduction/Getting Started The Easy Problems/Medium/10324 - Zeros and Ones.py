# user: Mousa-mahmood-hilal
#Problem: UVA 10324 - Zeros and Ones
count=0
while True:   
    try:
        s=input()
        print('Case '+str(count+1)+':')
        n=int(input())
        for k in range(n):
            i,j=map(int,input().split())
            mn=min(i,j)
            mx=max(i,j)
            ns=s[mn:mx+1]
            x=ns.count('0')
            if x==0 or x==mx+1-mn:
                print('Yes')
            else:
                print('No')
        count+=1
    except EOFError:
        break
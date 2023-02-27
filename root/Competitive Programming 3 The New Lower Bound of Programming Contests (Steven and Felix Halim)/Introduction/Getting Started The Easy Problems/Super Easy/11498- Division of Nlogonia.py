# user: Mousa-mahmood-hilal
#Problem: 11498 - Division of Nlogonia
while True:
    k=int(input())
    if not k:
        break
    n,m=map(int,input().split())
    for i in range(k):
        x,y=map(int,input().split())
        if x==n or y==m:
            print('divisa')
        elif x > n and y > m:
            print('NE')
        elif x < n and y > m:
            print('NO')
        elif x < n and y < m:
            print('SO')
        else:
            print('SE')
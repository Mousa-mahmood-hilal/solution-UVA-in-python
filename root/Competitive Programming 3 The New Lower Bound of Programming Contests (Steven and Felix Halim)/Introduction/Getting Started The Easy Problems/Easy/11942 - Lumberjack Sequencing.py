# user: Mousa-mahmood-hilal
#Problem: UVA 11942 - Lumberjack Sequencing
number_of_groups=int(input())
s=[]
for i in range(number_of_groups):
    l=0;g=0
    arr=list(map(int,input().split()))
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            l+=1
        else:
            break
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            g+=1
        else:
            break
    if l==len(arr)-1 or g==len(arr)-1:
        s.append('Ordered')
    else:
        s.append('Unordered')
print('Lumberjacks:\n'+'\n'.join(s))
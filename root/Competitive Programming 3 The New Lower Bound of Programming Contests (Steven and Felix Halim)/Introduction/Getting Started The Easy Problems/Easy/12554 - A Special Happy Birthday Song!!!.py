# user: Mousa-mahmood-hilal
#Problem: UVA 12554 - A Special "Happy Birthday" Song!!!
test_cases=int(input())
array=['Happy', 'birthday', 'to', 'you','Happy', 'birthday', 'to', 'you', 'Happy', 'birthday', 'to','Rujia' ,'Happy', 'birthday', 'to' ,'you']
name=[]
for i in range(test_cases):
    name.append(input())
j=0
i=0
f=False
while True:
    print(name[i] + ': ' + array[j])
    i+=1
    j+=1
    if i==test_cases:
        f=True
        i=0
    if f and j==len(array):
        break
    if j==len(array):
        j=0
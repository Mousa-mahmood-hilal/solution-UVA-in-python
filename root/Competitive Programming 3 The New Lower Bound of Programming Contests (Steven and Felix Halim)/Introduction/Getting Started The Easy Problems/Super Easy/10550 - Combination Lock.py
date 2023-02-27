# user: Mousa-mahmood-hilal
#Problem: 10550 - Combination Lock
while True:
    p=list(map(int,input().split()))
    res=False
    # to check for False list
    if p.count(False)==len(p):
        res=True
    if  res:
        break
# 1  turn the dial clockwise 2 full turns : here we put first=720=360*2
# 2 stop at the first number of the combination: here we put first+=((p[0]-p[1])+40)%40*9 The following mathematical relationship to calculate degrees
# 3 turn the dial counter-clockwise 1 full turn : here we put second=360
# 4 continue turning counter-clockwise until the 2nd number is reached:second+= ((p[2]-p[1])+40)%40*9 ,same on 2
# 5 turn the dial clockwise again until the 3rd number is reached :third=((p[2]-p[3])+40)%40*9
# 6 pull the shank and the lock will open:print(ans)
    first = 720
    first+=((p[0]-p[1])+40)%40*9
    second= 360
    second+= ((p[2]-p[1])+40)%40*9
    third=((p[2]-p[3])+40)%40*9
    ans=first+second+third
    print(int(ans))
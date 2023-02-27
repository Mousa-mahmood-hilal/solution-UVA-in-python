# user: Mousa-mahmood-hilal
#Problem: UVA 12468 - Zapping
while True:
    a,b=map(int,input().split())
    if a<0 and b<0:
        break
    print(min(abs(b-a),abs(100-max(b,a)+min(a,b))))
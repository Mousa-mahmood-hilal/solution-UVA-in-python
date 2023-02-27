# user: Mousa-mahmood-hilal
#Problem: UVA 11687 - Digits
while True:
    num = input()
    if num == "END":
        break
    if num == "1":
        print(1)
        continue
    ans = 1
    s = len(num)
    tmp = 0
    while True:
        if s == tmp:
            break
        tmp = s
        s = len(str(s))
        ans += 1
    print(ans)
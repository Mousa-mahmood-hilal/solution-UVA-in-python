# user: Mousa-mahmood-hilal
#Problem: UVA 621 - Secret Research
test_cases=int(input())
while test_cases:
    num=input()
    if len(num)<=2:
        print('+')
    else:
        if num[len(num)-2]=='3' and num[len(num)-1]=='5':
            print('-')
        elif num[0]=='9' and num[len(num)-1]=='4':
            print('*')
        else:
            print('?')
    test_cases-=1
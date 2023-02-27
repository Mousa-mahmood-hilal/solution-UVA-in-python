# user: Mousa-mahmood-hilal
#Problem: UVA 10424 - Love Calculator
while True:
    try:
        s=input().lower()
        s1=input().lower()
        sums=0;sums1=0
        for i in s:
            t=ord(i)-96
            if t<=26 and t>=1:
                sums+=t
        for i in s1:
            t=ord(i)-96
            if t<=26 and t>=1:
                sums1+=t
        while sums>=10:
            t=0
            while sums:
                t+=sums%10
                sums=sums//10
            sums=t
        while sums1>=10:
            t=0
            while sums1:
                t+=sums1%10
                sums1=sums1//10
            sums1=t
        if sums1<sums:
            print('{0:.2f}'.format(((sums1*100)/sums))+' %')
        else:
            print('{0:.2f}'.format(((sums*100)/sums1))+' %')
    except EOFError:
        break
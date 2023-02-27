# user: Mousa-mahmood-hilal
#Problem: 272 - TEX Quotes
count = 0
while True:
    try :
        n = input()
        a = []
        for i in n:
            if i == "\"":
                if count == 0:
                    a.append("``")
                    count = 1   
                else:
                    a.append("''")
                    count = 0
            else:
                a.append(i)
        print("".join(a))
    except EOFError:
        break
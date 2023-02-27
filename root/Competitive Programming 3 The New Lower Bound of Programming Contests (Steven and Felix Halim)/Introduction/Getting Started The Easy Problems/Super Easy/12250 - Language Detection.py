# user: Mousa-mahmood-hilal
#Problem: 12250 - Language Detection
j=0
dec={'HELLO':'ENGLISH','HOLA':'SPANISH','HALLO':'GERMAN','BONJOUR':'FRENCH','CIAO':'ITALIAN','ZDRAVSTVUJTE':'RUSSIAN'}
while True:
    s=input()
    if s=='#':
        break
    if s not in dec.keys():
        print('Case '+str(j+1)+': '+'UNKNOWN')
    else:
        print('Case '+str(j+1)+': '+dec[s])
    j+=1
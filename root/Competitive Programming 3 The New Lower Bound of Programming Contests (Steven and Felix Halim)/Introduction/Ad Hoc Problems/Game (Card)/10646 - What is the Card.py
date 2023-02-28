# user: Mousa-mahmood-hilal
#Problem: UVA 10646 - What is the Card
test_case=int(input())
i=0
while(test_case):
      s=list(map(str,input().split()))
      print('Case '+str(i+1)+': ' +s[32])
      i+=1    
      test_case-=1
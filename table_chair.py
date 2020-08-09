'''
Table Chair
'''
n=int(input())
l=[]
for i in range(0,n):
  a,b,c,d=[int(x) for x in input().split()]
  l1=[a,b,c,d]
  l.append(l1)
for i in l:
    if i[0]%4==0:
      print("0")
    elif i[0]%4==1:
      print(min(d,min((b+c),(b+b+b))))
    elif i[0]%4==2:
        print(min(c,min((b+b),(d+d))))
    elif i[0]%4==3:
          print(min(b,min((c+d),(d+d+d))))
    
      
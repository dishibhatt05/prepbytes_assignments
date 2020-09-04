t=int(input())
out=[]
for i in range(0,t):
  a=list(map(int,input().split()))
  out.append(a)
obj=[]
for i in out:
  obj.append(abs(11*i[1]-60*i[0])/2)
for i in obj:
  if i < 360-i:
    print(int(i))
  else:
    print(int(360-i))
    
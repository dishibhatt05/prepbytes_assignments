out=[]
m=[]
for i in range(0,int(input())):
  a,b,c,n=map(int, input().split()) 
  out.append([a,b,c])
  m.append(n)

for i,j in zip(out,m):
    while len(i)!=j:
        i.append(sum(i[-3:]))

for i in out:
    for j in i:
        print(j,end=" ")
    print()


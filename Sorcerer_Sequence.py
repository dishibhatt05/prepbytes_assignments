'''
Sorcerer Sequence
'''
n=int(input())
l=[]
for i in range(0,n):
  l.append(int(input()))
for k in l:
    print(k,end=" ")
    while k>1:
        if k%2==0:
            seq=int(k**(1/2))
            print(seq,end=" ")
            k=seq
        else:
            seq=int(k**(3/2))
            print(seq,end=" ")
            k=seq
    print()
     
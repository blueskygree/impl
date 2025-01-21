import sys
input=sys.stdin.readline

triangle=[n*(n+1)/2 for n in range(1,46)]
eureka=[0]*1001

for i in triangle:
    for j in triangle:
        for x in triangle:
            if i+j+x<=1000:
                eureka[int(i+j+x)]=1

k=int(input())
for _ in range(k):
    t=int(input())

    if eureka[t]==1:
        print(1)
    else:
        print(0)
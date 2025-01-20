import sys
input=sys.stdin.readline

n,m=map(int,input().split())
data=[list(input().rstrip()) for _ in range(n)]
count=[]

for a in range(n-7):
    for b in range(m-7):
        indexw=0
        indexb=0
        
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2==0:
                    if data[i][j]=='W':
                        indexw+=1
                    if data[i][j]=='B':
                        indexb+=1
                
                else:
                    if data[i][j]=='B':
                        indexw+=1
                    if data[i][j]=='W':
                        indexb+=1
        
        count.append(min(indexw,indexb))

print(min(count))

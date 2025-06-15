import sys
input=sys.stdin.readline

n=int(input())
data=[list(map(int,input().rstrip())) for _ in range(n)]

def dnc(x,y,n):
    check=data[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != data[i][j]:
                check=-1
                break
    
    if check==-1:
        print("(",end="")
        n=(n//2)
        dnc(x,y,n)
        dnc(x,y+n,n)
        dnc(x+n,y,n)
        dnc(x+n,y+n,n)
        print(")",end="")
    
    elif check==1:
        print("1",end="")
    else:
        print("0",end="")

dnc(0,0,n)
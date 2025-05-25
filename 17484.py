import sys
input=sys.stdin.readline
inf=sys.maxsize

n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]

dy=[-1,0,1]
ans=inf

def dfs(x,y,dec,cur):
    global ans

    if x==n-1:
        ans=min(ans,cur)
        return
    
    for i in range(3):
        nx=x+1
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and i != dec:
            dfs(nx,ny,i,cur+data[nx][ny])

for i in range(m):
    dfs(0,i,-1,data[0][i])

print(ans)
import sys
input=sys.stdin.readline

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*n for _ in range(n)]
answer=int(1e9)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def check(x,y):
    if visited[x][y]:
        return False
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0>nx or nx>=n or 0>ny or ny<=n or visited[nx][ny]:
            return False
    
    return True

def flower(x,y,flag):
    total=data[x][y]
    visited[x][y]=flag

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        visited[nx][ny]=flag
        total+=data[nx][ny]

    return total

def dfs(total,cnt):
    global answer

    if total>=answer:
        return 
    if cnt==3:
        answer=min(total,answer)
        return
    
    for x in range(1,n-1):
        for y in range(1,n-1):
            if check(x,y):
                record=flower(x,y,True)
                dfs(total+record,cnt+1)
                flower(x,y,False)

dfs(0,0)
print(answer)
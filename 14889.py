import sys
input=sys.stdin.readline

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
visited=[False]*n
result=1e9

def dfs(member,idx):
    global result

    if member==n//2:
        team_start=0
        team_link=0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team_start+=data[i][j]
                
                elif not visited[i] and not visited[j]:
                    team_link+=data[i][j]

        result=min(result,abs(team_start-team_link))
        return 
    
    else:
        for i in range(idx,n):
            if not visited[i]:
                visited[i]=True
                dfs(member+1,i+1)
                visited[i]=False

dfs(0,0)
print(result)
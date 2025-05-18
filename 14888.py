import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
data=list(map(int,input().split()))
maximum=-10**9
minimum=10**9

def dfs(total,cnt,plus,minus,mul,div):
    global maximum,minimum

    if cnt==(n-1):
        maximum=max(total,maximum)
        minimum=min(total,minimum)
        return 

    if plus:
        dfs(total+A[cnt+1],cnt+1,plus-1,minus,mul,div)
    if minus:
        dfs(total-A[cnt+1],cnt+1,plus,minus-1,mul,div)
    if mul:
        dfs(total*A[cnt+1],cnt+1,plus,minus,mul-1,div)
    if div:
        dfs(int(total/A[cnt+1]),cnt+1,plus,minus,mul,div-1)

dfs(A[0],0,data[0],data[1],data[2],data[3])
print(maximum)
print(minimum)
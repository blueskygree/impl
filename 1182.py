import sys
input=sys.stdin.readline
"""from itertools import combinations

n,s=map(int,input().split())
data=list(map(int,input().split()))
count=0

for i in range(1,len(data)+1):
    ncr=combinations(data,i)
    
    for j in ncr:
        if sum(j)==s:
            count+=1

print(count)"""

#1번 풀이: combinations 이용

n,s=map(int,input().split())
data=list(map(int,input().split()))
count=0

def dfs(index,current_sum):
    global count

    if index==n:
        return 
    
    current_sum+=data[index]

    if current_sum==s:
        count+=1

    dfs(index+1,current_sum)
    dfs(index+1,current_sum-data[index])

dfs(0,0)
print(count)


#2번째 풀이: 백트래킹 활용용    
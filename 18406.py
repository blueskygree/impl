import sys
input=sys.stdin.readline

n=list(input().rstrip())
onescore=0
twoscore=0

for i in range(len(n)//2):
    onescore+=int(n[i])
for j in range(len(n)//2,len(n)):
    twoscore+=int(n[j])

if onescore==twoscore:
    print("LUCKY")
else:
    print("READY")
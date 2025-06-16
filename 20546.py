import sys
input=sys.stdin.readline

coin=int(input())
data=list(map(int,input().split()))

def bnp(coin,cnt):
    for i in range(len(data)):
        if coin//data[i]>0:
            cnt+=coin//data[i]
            coin-=data[i]*cnt

    return cnt*(data[-1])+coin
    
def timing(coin,cnt):
    up_coin=0
    down_coin=0

    for i in range(1,len(data)):
        if data[i-1]<data[i]:
            up_coin+=1
            down_coin=0

        elif data[i-1]>data[i]:
            down_coin+=1
            up_coin=0
        
        else:
            up_coin=0
            down_coin=0
        
        if up_coin>=3:
            coin+=cnt*data[i]
            cnt=0
        elif down_coin>=3:
            if coin>=data[i]:
                cnt+=coin//data[i]
                coin-=data[i]*cnt

    return cnt*(data[-1])+coin

bnp_mon = bnp(coin,0)
tim_mon = timing(coin,0)

if bnp_mon > tim_mon:
    print("BNP")
elif bnp_mon < tim_mon:
    print("TIMING")
else:
    print("SAMESAME")
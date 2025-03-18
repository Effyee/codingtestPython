#준현
# 살 수 있을 때 즉시 최대 수량 매수
#성민
# 전량 매수, 전량 매도
# 3일 연속 가격이 오르면 전량 매도, 전일,오늘 주가가 동일하면 상승한 것이 아님
# 3일 연속 하락하면 전량 매수
# 기간 1월1일 부터 1월 14일까지
#결과: (현금+ 1월 14일의 주가 x 주식 수)

import sys
input=sys.stdin.readline
money=int(input())
chart=list(map(int,input().split()))

def sungmin(money):
    #상승날, 하락날,보유 주식 수, 현금
    up_days,down_days,stock,m=0,0,0,money
    for i in range(13):
        if up_days>=3:
            m+=stock*chart[i]
            stock=0
        elif down_days>=3:
            stock+=(m//chart[i])
            m=m-((m//chart[i])*chart[i])
        if chart[i]==chart[i+1]:
            continue
        elif chart[i]>chart[i+1]:
            up_days = 0
            down_days+=1
        else:
            up_days += 1
            down_days = 0
    return chart[-1]*stock+m

def junhuyn(money):
    stock,m=0,money
    for i in range(14):
        if chart[i]<=m:
            stock += (m // chart[i])
            m = m - ((m // chart[i]) * chart[i])
    return chart[-1] * stock + m

if junhuyn(money)>sungmin(money):
    print("BNP")
elif junhuyn(money)==sungmin(money):
    print("SAMESAME")
else:
    print("TIMING")




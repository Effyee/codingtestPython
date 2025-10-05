import sys
input=sys.stdin.readline

# 자연수 카드 n장
# x,y 번 카드를 골라 두 장에 쓰인 값을 계산
# x,y 카드 두 장에 모두 덮어 쓴다.

# m 번의 놀이 횟수, 점수를 가장 작게 만드는 것이 목표
n,m=map(int,input().split())
cards=list(map(int,input().split()))
cards.sort()
for i in range(m):
    total=cards[0]+cards[1]
    cards[0],cards[1]=total,total
    cards.sort()

print(sum(cards))
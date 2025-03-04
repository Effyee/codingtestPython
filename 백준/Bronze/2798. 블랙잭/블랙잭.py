import sys
input=sys.stdin.readline

N,M=map(int,input().split())
card=list(map(int,input().split()))
answer=-int(1e9)
cards=[]
visited=[False]*(N)

def backtrack():
    global answer
    if len(cards)==3:
        if sum(cards)<=M:
            answer=max(sum(cards),answer)
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            cards.append(card[i])
            backtrack()
            visited[i]=False
            cards.pop()

backtrack()
print(answer)

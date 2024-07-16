import sys
input=sys.stdin.readline
INF=int(1e9)

n=int(input())
numbers=list(map(int,input().split()))
plus,minus,mul,div=map(int,input().split())

maximum,minimum=-INF,INF

def dfs(result,idx,plus,minus,mul,div):
    global maximum
    global minimum
    if idx==n:
        maximum=max(maximum,result)
        minimum=min(minimum,result)
        return
    if plus>0:
        dfs(result+numbers[idx],idx+1,plus-1,minus,mul,div)
    if minus>0:
        dfs(result-numbers[idx],idx+1,plus,minus-1,mul,div)
    if mul>0:
        dfs(result*numbers[idx],idx+1,plus,minus,mul-1,div)
    if div>0:
        dfs(int(result/numbers[idx]),idx+1,plus,minus,mul,div-1)

dfs(numbers[0],1,plus,minus,mul,div)

print(maximum, minimum)

import sys

n=int(input())
number=list(map(int,sys.stdin.readline().split()))
add,sub,mul,div=map(int,sys.stdin.readline().split())

max_result=-int(1e9)
min_result=int(1e9)

def dfs(add,sub,mul,div,sum,idx):
    global max_result, min_result
    if idx==n:
        max_result= max(sum,max_result)
        min_result=min(sum,min_result)
        return

    if add:
        dfs(add-1,sub,mul,div,sum+number[idx],idx+1)
    if sub:
        dfs(add,sub-1,mul,div,sum-number[idx],idx+1)
    if mul:
        dfs(add,sub,mul-1,div,sum*number[idx],idx+1)
    if div:
        dfs(add,sub,mul,div-1,int(sum/number[idx]),idx+1)

dfs(add,sub,mul,div,number[0],1)
print(max_result)
print(min_result)
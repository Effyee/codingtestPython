def dfs(result,index,cnt):
    global answer
    if index==n:
        if result==s and cnt>0:
            answer+=1
        return

    dfs(result,index+1,cnt)
    dfs(result+numbers[index],index+1,cnt+1)

n,s=map(int,input().split())
numbers=list(map(int,input().split()))
answer=0
dfs(0,0,0)
print(answer)
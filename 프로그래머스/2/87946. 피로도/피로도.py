answer=0
def dfs(dungeons,stress,visited,cnt):
    global answer
    answer=max(answer,cnt)
    for i in range(len(dungeons)):
        if stress>=dungeons[i][0] and not visited[i]:
            visited[i]=True
            dfs(dungeons,stress-dungeons[i][1],visited,cnt+1)
            visited[i]=False

def solution(k, dungeons):
    global answer
    visited=[False]*len(dungeons)
    dfs(dungeons,k,visited,0)
    return answer
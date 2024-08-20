from collections import deque

def check(word1,word2):
    count=0
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            count+=1
    if count==1:
        return True
    return False

def bfs(words,visited,begin,target):
    q=deque()
    q.append([begin,0])

    while q:
        now,count=q.popleft()
        if now==target:
            return count
        for i in range(len(words)):
            if not visited[i]:
                if check(now,words[i]):
                    visited[i]=True
                    q.append((words[i],count+1))


def solution(begin, target, words):
    if target not in words:
        return 0
    visited=[False]*len(words)
    answer=bfs(words,visited,begin,target)
    return answer
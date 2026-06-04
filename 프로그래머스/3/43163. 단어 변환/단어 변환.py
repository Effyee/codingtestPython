from collections import deque
def solution(begin, target, words):
    answer = 0
    visited=[False]*len(words);
    
    if target not in words:
        return 0
    
    def check(now,word):
        diff=0;
        for n,w in zip(now,word):
            if n!=w:
                diff+=1
        if diff==1:
            return True
        return False
    
    def bfs():
        q=deque()
        q.append((begin,0))
        while q:
            w,c=q.popleft();
            if w==target:
                return c
            
            for i in range(len(words)):
                if not visited[i]:
                    if check(words[i],w):
                        visited[i]=True
                        q.append((words[i],c+1))        
        
    answer=bfs()
    return answer
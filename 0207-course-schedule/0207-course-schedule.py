from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses

        for pre in prerequisites:
            a,b=pre
            graph[a].append(b)
            indegree[b]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        if not q:
            return False
        
        while q:
            now=q.popleft()
            for node in graph[now]:
                indegree[node]-=1
                if indegree[node]==0:
                    q.append(node)
        if sum(indegree)==0:
            return True
        return False
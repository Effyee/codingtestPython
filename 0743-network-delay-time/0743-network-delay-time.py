import heapq
INF=int(1e9)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = [INF] * (n+1)
        distances[k] = 0
        
        pq = [(0, k)]
        
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            
            if curr_dist > distances[curr_node]:
                continue
            
            for next_node, weight in graph[curr_node]:
                distance = curr_dist + weight
                
                if distance < distances[next_node]:
                    distances[next_node] = distance
                    heapq.heappush(pq, (distance, next_node))
        
        max_distance = max(distances[1:])
        
        if max_distance!=INF:
            return max_distance
        return -1

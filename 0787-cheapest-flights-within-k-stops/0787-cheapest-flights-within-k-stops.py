import heapq
INF = int(1e9)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for dep, arr, cost in flights:
            graph[dep].append((arr, cost))
        
        visited = [[INF, 0] for _ in range(n)]
        
        pq = [(0, src, k + 1)]  # (가격, 노드, 남은 경유지 개수)
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            if node == dst:
                return cost
            
            if stops > 0:
                for next_node, next_cost in graph[node]:
                    new_cost = cost + next_cost
                    if new_cost < visited[next_node][0] or stops - 1 > visited[next_node][1]:
                        visited[next_node] = [new_cost, stops - 1]
                        heapq.heappush(pq, (new_cost, next_node, stops - 1))
        
        return -1

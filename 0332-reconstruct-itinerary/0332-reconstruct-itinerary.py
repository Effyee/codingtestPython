from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for dep, arr in sorted(tickets, reverse=True):
            graph[dep].append(arr)
        
        route = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            route.append(airport)
        
        dfs("JFK")
        return route[::-1]

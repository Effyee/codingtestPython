class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        answer = 0
        
        def dfs(i, j):
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            visited[i][j] = True
            
            for direction in range(4):
                nx = i + dx[direction]
                ny = j + dy[direction]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if not visited[nx][ny] and grid[nx][ny] == '1':
                        dfs(nx, ny)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i, j)
                    answer += 1
                    
        return answer

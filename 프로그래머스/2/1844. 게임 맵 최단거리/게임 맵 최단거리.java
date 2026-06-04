import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        // bfs 결과를 받아와서 리턴
        return bfs(maps);
    }
    
    int bfs(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        Queue<int[]> q = new LinkedList<>();

        // 시작 칸을 1로 잡는 경우가 많습니다 (문제 조건 확인 필요)
        q.offer(new int[]{0, 0, 1}); 
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        
        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0];
            int y = curr[1];
            int distance = curr[2];
            
            if (x == n - 1 && y == m - 1) {
                return distance;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i]; // 정확한 이동
                int ny = y + dy[i]; // 정확한 이동
                
                // 범위 체크 및 벽(0) 확인, 방문 여부 확인
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && maps[nx][ny] == 1) {
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx, ny, distance + 1});
                }
            }
        }
        return -1; // 목적지에 도달할 수 없는 경우
    }
}
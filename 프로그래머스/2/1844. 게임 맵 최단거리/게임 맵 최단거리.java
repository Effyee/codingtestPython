import java.util.*;
class Solution {

    class Node{
        int x;
        int y;
        int dist;

        Node(int x, int y, int dist){
            this.x = x;
            this.y = y;
            this.dist=dist;
        }
    }

    public int solution(int[][] maps) {
        return bfs(maps);
    }

    int bfs(int[][] maps){

        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0, 0, 1));

        boolean[][] visited =
                new boolean[maps.length][maps[0].length];
        
        visited[0][0]=true;
            
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        while(!q.isEmpty()){
            Node now = q.poll();
            int dist=now.dist;
            
            if(now.x==maps.length-1 && now.y==maps[0].length-1){
                return dist;
            }
            
            for(int i=0;i<4;i++){
                int nx=now.x+dx[i];
                int ny=now.y+dy[i];
                if(nx>=0 && nx<maps.length && ny>=0 && ny<maps[0].length
                  && !visited[nx][ny] && maps[nx][ny]==1){
                    visited[nx][ny]=true;
                    q.offer(new Node(nx,ny,dist+1));
                }
            }
            
            
        }

        return -1;
    }
}
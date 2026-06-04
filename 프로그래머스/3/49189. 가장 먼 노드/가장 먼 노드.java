import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        List<List<Integer>> graph = new ArrayList<>();

        for(int i = 0; i <= n; i++){
            graph.add(new ArrayList<>());
        }

        for(int[] e : edge){
            int a = e[0];
            int b = e[1];

            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        
        int[] distance=new int[n+1];
        Arrays.fill(distance,n+1);
        distance[0]=0;
        Queue<Integer>q=new LinkedList<>();
        q.offer(1);
        distance[1]=0;
        
        while(!q.isEmpty()){
            int now=q.poll();
            for(int next_node:graph.get(now)){
                if(distance[next_node]>distance[now]+1){
                    distance[next_node]=distance[now]+1;
                    q.offer(next_node);                      
                }
            }
        }
        
        Arrays.sort(distance);
        int max_distance=distance[distance.length-1];
        
        for(int dist:distance){
            if(dist==max_distance){
                answer++;
            }
        }
        return answer;
    }
}
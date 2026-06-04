import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        int[] distance=new int[n+1];
        Arrays.fill(distance,n+1);
        distance[0]=0;
        List<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for(int[] e : edge) {
            int num1 = e[0];
            int num2 = e[1];
            graph.get(num1).add(num2);
            graph.get(num2).add(num1);
        }
        Queue<Integer>q=new LinkedList<>();
        q.offer(1);
        distance[1]=0;
        while(!q.isEmpty()){
            int now=q.poll();
            for(int next:graph.get(now)){
                if(distance[next]>distance[now]+1){
                    distance[next]=distance[now]+1;
                    q.offer(next);
                }
            }
        }
        Arrays.sort(distance);
        int max=distance[n];
        for(int a:distance){
            if(max==a){
            answer++;}
        }
        return answer;
    }
}
import java.util.*;

class Solution {
    class Node{
        int time;
        int cnt;
        Node(int time, int cnt){
            this.time=time;
            this.cnt=cnt;
        }
    }
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int active=0;
        Queue<Node> q=new LinkedList<>();
        for(int player:players){
            while(!q.isEmpty()&& q.peek().time == 0){
                    active-=q.peek().cnt;
                    q.poll();
            }
            for(int i=0;i<q.size();i++){
                Node n=q.poll();
                q.offer(new Node(n.time-1, n.cnt));
            }
            
            int need=player/m;
            if(need>active){
                int add=need-active;
                
                answer += add;
                active += add;

                q.offer(new Node(k - 1, add));
            }
        }
        return answer;
    }
}
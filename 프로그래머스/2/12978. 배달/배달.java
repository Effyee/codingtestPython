import java.util.*;

class Solution {

    static class Node {
        int v;
        int cost;

        Node(int v, int cost) {
            this.v = v;
            this.cost = cost;
        }
    }

    public int solution(int N, int[][] road, int K) {

        List<ArrayList<Node>> graph = new ArrayList<>();

        for(int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        for(int[] r : road) {
            int a = r[0];
            int b = r[1];
            int cost = r[2];

            graph.get(a).add(new Node(b, cost));
            graph.get(b).add(new Node(a, cost));
        }

        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        PriorityQueue<Node> pq =
                new PriorityQueue<>((a, b) -> a.cost - b.cost);

        dist[1] = 0;
        pq.offer(new Node(1, 0));

        while(!pq.isEmpty()) {

            Node now = pq.poll();

            if(now.cost > dist[now.v]) continue;

            for(Node next : graph.get(now.v)) {

                if(dist[next.v] > dist[now.v] + next.cost) {

                    dist[next.v] = dist[now.v] + next.cost;

                    pq.offer(
                        new Node(next.v, dist[next.v])
                    );
                }
            }
        }

        int answer = 0;

        for(int i = 1; i <= N; i++) {
            if(dist[i] <= K) answer++;
        }

        return answer;
    }
}
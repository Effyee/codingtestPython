import java.util.*;

class Solution {

    public int solution(int bridge_length, int weight, int[] truck_weights) {

        Queue<Integer> bridge = new LinkedList<>();

        int time = 0;
        int curWeight = 0;
        int idx = 0;

        // 다리 초기 상태
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }

        while (!bridge.isEmpty()) {

            time++;

            // 한 칸 이동
            curWeight -= bridge.poll();

            // 다음 트럭 올릴 수 있으면
            if (idx < truck_weights.length &&
                curWeight + truck_weights[idx] <= weight) {

                bridge.offer(truck_weights[idx]);
                curWeight += truck_weights[idx];
                idx++;
            }
            else {
                bridge.offer(0);
            }

            // 모든 트럭 끝났으면 종료
            if (idx == truck_weights.length && curWeight == 0) {
                break;
            }
        }

        return time;
    }
}
import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {

        int answer = 0;

        Queue<Integer> q = new LinkedList<>();
        Queue<Integer> idx = new LinkedList<>();

        // queue 초기화
        for (int i = 0; i < priorities.length; i++) {
            q.offer(priorities[i]);
            idx.offer(i);
        }

        while (!q.isEmpty()) {

            int max = Collections.max(q);

            // 현재 프로세스 꺼내기
            int cur = q.poll();
            int curIdx = idx.poll();

            // 더 높은 우선순위 존재
            if (cur < max) {
                q.offer(cur);
                idx.offer(curIdx);
            }
            else {
                answer++;

                // 내가 찾는 프로세스면 종료
                if (curIdx == location) {
                    return answer;
                }
            }
        }

        return answer;
    }
}
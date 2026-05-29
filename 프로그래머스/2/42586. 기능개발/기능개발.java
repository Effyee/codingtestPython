import java.util.*;

class Solution {

    public int[] solution(int[] progresses, int[] speeds) {

        ArrayList<Integer> list = new ArrayList<>();

        Stack<Integer> stck = new Stack<>();

        // 작업 완료일까지 계산
        for (int i = progresses.length - 1; i >= 0; i--) {

            int spend = (int)Math.ceil(
                (double)(100 - progresses[i]) / speeds[i]
            );

            stck.push(spend);
        }

        while (!stck.isEmpty()) {

            int standard = stck.pop();

            int count = 1;

            while (!stck.isEmpty() && stck.peek() <= standard) {
                stck.pop();
                count++;
            }

            list.add(count);
        }

        // ArrayList -> int[]
        int[] answer = new int[list.size()];

        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}
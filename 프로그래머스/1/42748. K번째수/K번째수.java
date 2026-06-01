import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {

        int[] answer = new int[commands.length];

        for (int i = 0; i < commands.length; i++) {

            int start = commands[i][0] - 1; // i
            int end = commands[i][1];       // j
            int k = commands[i][2] - 1;     // k

            int[] temp = Arrays.copyOfRange(
                array,
                start,
                end
            );

            Arrays.sort(temp);

            answer[i] = temp[k];
        }

        return answer;
    }
}
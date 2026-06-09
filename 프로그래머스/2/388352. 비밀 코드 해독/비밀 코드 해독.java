import java.util.*;

class Solution {

    int answer = 0;

    public int solution(int n, int[][] q, int[] ans) {

        ArrayList<Integer> nums = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            nums.add(i);
        }

        combination(nums, 5, 0, new ArrayList<>(), q, ans);

        return answer;
    }

    void combination(ArrayList<Integer> nums,
                     int count,
                     int idx,
                     ArrayList<Integer> comb,
                     int[][] q,
                     int[] ans) {

        if (comb.size() == count) {

            if (check(comb, q, ans)) {
                answer++;
            }

            return;
        }

        for (int i = idx; i < nums.size(); i++) {

            comb.add(nums.get(i));

            combination(nums,
                        count,
                        i + 1,
                        comb,
                        q,
                        ans);

            comb.remove(comb.size() - 1);
        }
    }

    boolean check(ArrayList<Integer> comb,
                  int[][] q,
                  int[] ans) {

        for (int i = 0; i < q.length; i++) {

            int cnt = 0;

            for (int num : q[i]) {

                if (comb.contains(num)) {
                    cnt++;
                }
            }

            if (cnt != ans[i]) {
                return false;
            }
        }

        return true;
    }
}
import java.util.*;

class Solution {
    boolean solution(String s) {

        Stack<Character> stck = new Stack<>();

        for (int i = 0; i < s.length(); i++) {

            if (s.charAt(i) == '(') {
                stck.push(s.charAt(i));
            } else {

                if (stck.isEmpty()) {
                    return false;
                }

                stck.pop();
            }
        }

        return stck.isEmpty();
    }
}
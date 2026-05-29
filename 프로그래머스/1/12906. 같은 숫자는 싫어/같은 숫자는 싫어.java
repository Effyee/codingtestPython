import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        
        Stack<Integer>stck=new Stack<>();
        for(int i=0;i<arr.length;i++){
            if(stck.isEmpty()){
                stck.push(arr[i]);
            }else{
                if(stck.peek()!=arr[i]){
                    stck.push(arr[i]);
                }
            }
        }
        
        int[] answer = new int[stck.size()];
        for(int i=0;i<stck.size();i++){
            answer[i]=stck.get(i);
        }
        return answer;
    }
}
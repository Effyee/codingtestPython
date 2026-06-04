class Solution {
    int answer = 0;
    public int solution(int[] numbers, int target) {
        
        dfs(0,numbers,target,0);
        
        return answer;
    }
    
    public void dfs(int result, int[] numbers, int target, int idx){
        if(idx==numbers.length){
            if(target==result){
                answer++;
            }
            return;
        }
        dfs(result+numbers[idx],numbers,target,idx+1);
        dfs(result-numbers[idx],numbers,target,idx+1);
    }
}
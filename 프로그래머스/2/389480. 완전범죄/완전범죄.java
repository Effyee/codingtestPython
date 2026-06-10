class Solution {
    public int solution(int[][] info, int n, int m) {
        int INF=1000000000;
        int answer = INF;
        int[] dp=new int[m];
        
        for(int i=0;i<m;i++){
            dp[i]=INF;
        }
        dp[0]=0;
        
        for(int[] infos:info){
            int a_trace=infos[0];
            int b_trace=infos[1];
            
            int[] new_dp=new int[m];
            
            for(int i=0;i<m;i++){
                new_dp[i]=INF;
            }
            
            for(int prev_b=0;prev_b<m;prev_b++){
                if(dp[prev_b]==INF){
                    continue;
                }
                //A가 훔침
                int a_new=a_trace+dp[prev_b];
                if(a_new<n){
                    new_dp[prev_b]=Math.min(a_new,new_dp[prev_b]);
                }
                //B가 훔침
                int b_new=prev_b+b_trace;
                if(b_new<m){
                    new_dp[b_new]=Math.min(dp[prev_b],new_dp[b_new]);
                }
                
            }
            dp=new_dp;
        }
        for(int i=0;i<dp.length;i++){
            if(dp[i]<answer){
                answer=dp[i];
            }
        }
        if(answer==INF){
            return -1;
        }
        return answer;
    }
}
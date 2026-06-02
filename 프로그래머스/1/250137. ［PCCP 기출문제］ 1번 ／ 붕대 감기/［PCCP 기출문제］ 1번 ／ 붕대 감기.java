class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        
        //보너스 받기위한 시전시간
        int t=bandage[0];
        //회복량
        int x=bandage[1];
        //보너스 회복량
        int y=bandage[2];
        //최대 회복량
        int max_health=health;
        
        int last_time=attacks[attacks.length-1][0];
        int attack_index=0;
        int continued_index=0;
        
        for(int time=1; time<=last_time; time++){
            if(attacks[attack_index][0]==time){
                health-=attacks[attack_index][1];
                if(health<=0){
                    return -1;
                }
                attack_index++;
                continued_index=0;
            }
            else{
                health+=x;
    
                continued_index++;
                if(continued_index==t){
                    health+=y;
                    continued_index=0;
                }
                
                if(health>=max_health){
                    health=max_health;
                }
            }
        
        }
        
        return health;
    }
}
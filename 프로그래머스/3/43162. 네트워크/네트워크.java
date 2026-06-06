import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
       
        int[] parent=new int[n];
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i!=j && computers[i][j]==1){
                    make_union(i,j,parent);
                }
            }
        }
        
        for(int i=0;i<n;i++){
            find_parent(i,parent);
        }
        
        HashSet<Integer> s=new HashSet<>();
        for(int i=0;i<n;i++){
            s.add(parent[i]);
        }
        
        return s.size();
    }
    
    int find_parent(int x, int[]parent){
        if(parent[x]!=x){
            parent[x]=find_parent(parent[x],parent);
        }
        return parent[x];
    }
    
    void make_union(int a, int b, int[]parent){
        a=find_parent(a,parent);
        b=find_parent(b,parent);
        
        if(a<b){
            parent[b]=a;
        }
        else{
            parent[a]=b;
        }
    }
}
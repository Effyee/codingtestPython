import java.util.*;
class Solution {
    int[] parent;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        parent = new int[n];
        
        for(int i = 0; i < n; i++){
            parent[i] = i;
        }
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(computers[i][j]==1 && i!=j){
                    make_union(i,j,parent);
                }
            }
        }
        
        
        HashSet<Integer> s=new HashSet<>();
        for(int i = 0; i < n; i++) {
            s.add(find_parent(parent, i));
        }
        return s.size();
    }
    
    int find_parent(int[] parent, int x){
        if(parent[x]!=x){
            parent[x]=find_parent(parent,parent[x]);
        }
        return parent[x];
        
    }
    
    void make_union(int a, int b, int[] parent){
        a=find_parent(parent,a);
        b=find_parent(parent,b);
        
        if(a<b){
            parent[b]=a;
        }
        else{
            parent[a]=b;
        }
    }
    
}
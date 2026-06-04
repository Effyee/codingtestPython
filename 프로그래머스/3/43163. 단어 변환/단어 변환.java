import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        answer=bfs(begin, target, words);
        return answer;
    }
    
    boolean check(String next_word, String current_word){
        
        int diff=0;
        for(int i=0;i<next_word.length();i++){
            if (next_word.charAt(i)!=current_word.charAt(i)){
                diff+=1;
            }
        }
        
        if(diff==1){
            return true;
        }
        
        return false;
    }
    class Node{
        String word;
        int count;
        public Node(String word, int count){
            this.word=word;
            this.count=count;            
        }
    }
    int bfs(String begin,String target,String[] words){
        Queue<Node> q=new LinkedList<>();
        boolean[] visited=new boolean[words.length];
        q.offer(new Node(begin,0));
        while(!q.isEmpty()){
            Node curr = q.poll();
            String current_word = curr.word;
            int count = curr.count;
            
            if(current_word.equals(target)){
                return count;
            }
            
            for(int i=0;i<words.length;i++){
                if(check(words[i],current_word) && !visited[i]){
                    visited[i]=true;
                    q.offer(new Node(words[i],count+1));
                }
            }
        }
        return 0;
    }
}
#include <string>
#include <vector>
#include <iostream>
#include <functional>
#include <deque>
#include <utility>
using namespace std;

bool word_diff(string a, string b){
    //모든 단어의 길이는 같음
    int n=a.size();
    int diff=0;
    for(int i=0;i<n;i++){
        if(a[i]!=b[i]){
            diff+=1;
        }
    }
    return diff==1;
}

int bfs(string begin, string target,vector<string> &words){
    deque<pair<string,int>> dq;
    dq.push_back({begin,0});
    vector<bool>visited(words.size(),false);
    
    while(!dq.empty()){
        pair<string,int> curr=dq.front();
        dq.pop_front();
        string cword=curr.first;
        int count=curr.second;
        if(cword==target){
            return count;
        }
        
        for(int i=0;i<words.size();i++){
            if(!visited[i]&&word_diff(cword,words[i])){
                visited[i]=true;
                dq.push_back({words[i],count+1});
            }
        }
        
    }
    return 0;
    
}

int solution(string begin, string target, vector<string> words) {
    return bfs(begin,target,words);
}
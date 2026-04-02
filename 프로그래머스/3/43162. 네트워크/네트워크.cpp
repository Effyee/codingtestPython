#include <string>
#include <vector>
#include <functional>
#include <iostream>
using namespace std;

void dfs(int start,const vector<vector<int>>& computers,vector<bool>&visited){
    visited[start]=true;
    for(int j=0;j<computers.size();j++){
        if (computers[start][j]==1&!visited[j]){
            visited[j]=true;
            dfs(j,computers,visited);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    n=computers.size();
    vector<bool> visited(n,false);
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, computers, visited); 
            answer++; 
        }
    }
    return answer;
}
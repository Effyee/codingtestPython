#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int find_parent(vector<int>&parent, int x){
    if(parent[x]!=x){
        parent[x]=find_parent(parent,parent[x]);
    }
    return parent[x];
}

void make_union(int a, int b, vector<int> &parent){
    a=find_parent(parent,a);
    b=find_parent(parent,b);
    
    if(a<=b)parent[b]=a;
    else parent[a]=b;
    
    return;
}


int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    vector<int> parent(n); 
    for (int i = 0; i < n; i++) {
        parent[i] = i;    
    }
    sort(costs.begin(), costs.end(), [](const vector<int>& a, const vector<int>& b) {
    return a[2] < b[2];
    });
    
    for(auto&edge:costs){
        int start=edge[0];
        int end=edge[1];
        int cost=edge[2];
        if(find_parent(parent,start)!=find_parent(parent,end)){
            answer+=cost;
            make_union(start,end,parent);
        }
    }
    
    return answer;
}
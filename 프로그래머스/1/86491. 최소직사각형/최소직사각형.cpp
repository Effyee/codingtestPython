#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    priority_queue<int> row;
    priority_queue<int> col;
    int n=sizes.size();
    for(int i=0;i<n;i++){
        sort(sizes[i].begin(),sizes[i].end());
        row.push(sizes[i][0]);
        col.push(sizes[i][1]);
    }
    return row.top()*col.top();
}
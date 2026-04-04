#include <string>
#include <queue>
#include <functional>
#include <iostream>
#include <vector>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq(scoville.begin(),scoville.end());
    
    while(pq.top()<K){
        if(pq.size()<=1){
            return -1;
        }
        int f=pq.top();
        pq.pop();
        int s=pq.top();
        pq.pop();
        int t=f+s*2;
        pq.push(t);
        answer++;
    }
    
    return answer;
}
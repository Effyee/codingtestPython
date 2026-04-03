#include <string>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq(scoville.begin(),scoville.end());
    while (pq.top()<K){
        if (pq.size() < 2) return -1;
        int a=pq.top();
        pq.pop();
        int b=pq.top();
        pq.pop();
        
        int c = a + (b * 2);
        pq.push(c);
        answer++;
    }
    return answer;
}
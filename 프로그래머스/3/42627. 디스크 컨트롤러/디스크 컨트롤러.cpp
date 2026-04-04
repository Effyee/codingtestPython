#include <string>
#include <vector>
#include <tuple>
#include <algorithm>
#include <iostream>
#include <functional>
#include <queue>
using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    
    // [작업이 요청되는 시점, 작업의 소요시간] 정렬
    sort(jobs.begin(),jobs.end(),[](auto a, auto b){
        return a[0]<b[0];
    });
    for(auto &x:jobs){
         cout << x[0] << " " << x[1] << endl;
    }
    //현재 시각
    int time=0;
    //처리된 작업의 수
    int n=0;
    int i=0;
    priority_queue<tuple<int,int,int>,vector<tuple<int,int,int>>,greater<tuple<int,int,int>>> pq;
    int total=0;
    while(n<jobs.size()){
        //현재 시각 기준으로 요청된 작업을 다 우선순위 큐(min heap)에 넣기
        while(i < jobs.size() && jobs[i][0] <= time){
            // 우선순위
            // 1. 작업의 소요시간이 짧은것
            // 2. 작업의 요청 시각이 빠른 것
            // 3. 작업의 번호가 작은 것
            if(jobs[i][0]<=time){
                int s=jobs[i][0];
                int l=jobs[i][1];
                int idx=i;
                pq.push({l,s,idx});
                i++;
            }
        }
        if(pq.empty()){
            time = jobs[i][0];
            continue;
            }
        tuple<int,int,int> curr=pq.top();
        pq.pop();
        int cl=get<0>(curr);
        int cs=get<1>(curr);
        int cidx=get<2>(curr);
        
        
        time+=cl;
        total+=(time-cs);
        n++;
        
    }
    
    return total/n;
}
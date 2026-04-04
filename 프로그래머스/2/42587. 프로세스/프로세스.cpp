#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> priorities, int location) {
    queue<pair<int,int>> q;

    // (우선순위, 인덱스)
    for(int i = 0; i < priorities.size(); i++){
        q.push({priorities[i], i});
    }

    int answer = 0;

    while(!q.empty()){
        auto curr = q.front();
        q.pop();

        bool hasHigher = false;

        // 큐 안에 더 높은 우선순위 있는지 확인
        queue<pair<int,int>> temp = q;
        while(!temp.empty()){
            if(temp.front().first > curr.first){
                hasHigher = true;
                break;
            }
            temp.pop();
        }

        if(hasHigher){
            q.push(curr); // 다시 뒤로
        } else {
            answer++; // 실행됨

            if(curr.second == location){
                return answer;
            }
        }
    }

    return answer;
}
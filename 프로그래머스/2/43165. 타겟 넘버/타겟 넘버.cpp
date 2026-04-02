#include <string>
#include <vector>
#include <functional>

using namespace std;

void dfs(const vector<int>&numbers, int target, int& answer, int idx, int total){
    if(idx==numbers.size()){
        if(total==target){
            answer+=1;
        }
        return;
    }
    dfs(numbers,target,answer,idx+1,total+numbers[idx]);
    dfs(numbers,target,answer,idx+1,total-numbers[idx]);
}

int solution(vector<int> numbers, int target) {
    int answer = 0;
    dfs(numbers,target,answer,0,0);
    return answer;
}
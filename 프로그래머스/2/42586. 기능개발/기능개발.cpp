#include <string>
#include <vector>
#include <queue>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int n=progresses.size();
    vector<int> s(n,0);
    for(int i=0;i<n;i++){
        int l=(100-progresses[i]+speeds[i]-1)/speeds[i];
        s[i]=l;
    }
    int count=1;
    int standard=s[0];
    for(int j=1;j<n;j++){
        if(standard>=s[j]){
            count++;
        }
        else{
            answer.push_back(count);
            standard=s[j];
            count=1;
        }
    }
    answer.push_back(count);
    return answer;
}
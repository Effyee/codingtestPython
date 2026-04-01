#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(int i=0;i<commands.size();i++){
        int s=commands[i][0];
        int e=commands[i][1];
        int k=commands[i][2];
        
        vector<int> sliced_array(array.begin()+(s-1),array.begin()+e);
        sort(sliced_array.begin(),sliced_array.end());
        answer.push_back(sliced_array[k-1]);
    }
    
    return answer;
}
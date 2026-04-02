#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> stack;
    
    for(int i=0;i<arr.size();i++){
        if(stack.size()==0){
            stack.push_back(arr[i]);
        }
        else{
            if(stack[stack.size()-1]!=arr[i]){
                stack.push_back(arr[i]);
            }
        }
    }

    return stack;
}
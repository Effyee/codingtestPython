#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    unordered_map <string,int> p;
    unordered_map <string,int> c;
    for (string par:participant){
        p[par]+=1;
    }
    for (string com:completion){
        c[com]+=1;
    }
    for(string par:participant){
        if (p[par]!=c[par]){
            return par;
        }
    }
}
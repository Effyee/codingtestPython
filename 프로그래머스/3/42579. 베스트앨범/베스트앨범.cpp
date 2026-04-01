#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    // 장르: 재생횟수
    unordered_map<string,int> g;
    // 장르: 재생횟수, 음악번호
    unordered_map<string,vector<pair<int,int>>> c;
    
    for(int i=0;i<genres.size();i++){
        g[genres[i]]+=plays[i];
        c[genres[i]].push_back({plays[i],i});
    }
    // 1. 장르별 총 재생수를 기준으로 장르 정렬하기
    // 정렬된 장르를 넣을 수 있도록 
    vector<pair<string, int>> sorted_g(g.begin(), g.end());
    sort(sorted_g.begin(), sorted_g.end(), [](auto a, auto b) {
        return a.second > b.second;
    });
    
    // 2. 정렬된 장르 내에서 노래 고르기
    for(auto const&[genre,play]:sorted_g){
        //현재 장르
        // 재생횟수 순, 재생횟수 같으면 이름 순
        vector<pair<int, int>>& songs = c[genre];
        sort(songs.begin(),songs.end(),[](auto a, auto b){
            if (a.first==b.first){
                return a.second<b.second;
            }
            return a.first>b.first;
        });
            for(int i = 0; i < songs.size() && i < 2; i++) {
            answer.push_back(songs[i].second);
        }
    }
        
    return answer;
}
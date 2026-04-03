#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    sort(times.begin(), times.end());

    // 1. 모든 시간 관련 변수는 long long으로!
    long long start = 1; 
    // 가장 오래 걸리는 경우: 가장 느린 심사관이 혼자 다 할 때
    long long end = (long long)times.back() * n; 
    
    while (start <= end) {
        long long mid = (start + end) / 2;
        long long p = 0; // 검사 가능한 총 인원수도 long long

        for (int i = 0; i < times.size(); i++) {
            p += (mid / times[i]);
            
            // 2. 팁: 이미 n을 넘었다면 굳이 더 더할 필요 없음 (오버플로우 방지)
            if (p >= n) break; 
        }

        if (p >= n) {
            answer = mid; // n명 이상 검사 가능하면 시간을 더 줄여봄
            end = mid - 1;
        } else {
            start = mid + 1; // n명 검사 못 하면 시간을 늘림
        }
    }
    return answer;
}
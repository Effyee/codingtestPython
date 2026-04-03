#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int n = jobs.size();

    // 1. 원본 jobs를 "요청 시각" 순으로 정렬 (먼저 들어온 놈부터 대기 큐에 넣기 위해)
    sort(jobs.begin(), jobs.end());

    // 2. 대기 큐 (소요시간, 요청시각, 인덱스) -> 소요시간 짧은 순 정렬
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;

    int time = 0;   // 현재 시각
    int idx = 0;    // jobs 배열을 훑을 인덱스
    int count = 0;  // 완료된 작업 개수

    while (count < n) {
        // 3. 현재 시각까지 들어온 모든 요청을 대기 큐에 push
        while (idx < n && jobs[idx][0] <= time) {
            pq.push({jobs[idx][1], jobs[idx][0], idx});
            idx++;
        }

        if (!pq.empty()) {
            // 4. 대기 큐에서 가장 빨리 끝나는 작업 수행
            auto curr = pq.top();
            pq.pop();

            int spend = get<0>(curr);
            int request = get<1>(curr);

            time += spend;           // 작업 처리 후 시각 업데이트
            answer += (time - request); // 반환 시간 = 종료 시각 - 요청 시각
            count++;
        } else {
            // 5. 대기 큐가 비어있다면, 다음 작업이 들어올 시각으로 점프
            time = jobs[idx][0];
        }
    }

    return answer / n;
}
#include <vector>
#include <tuple>
#include <deque>

using namespace std;

int bfs(vector<vector<int>>& maps) {
    int n = maps.size();
    int m = maps[0].size();
    
    deque<tuple<int, int, int>> dq;
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    
    visited[0][0] = true;
    dq.push_back({0, 0, 1}); 

    int dx[] = {0, 0, -1, 1};
    int dy[] = {-1, 1, 0, 0};
    
    while (!dq.empty()) {
        tuple<int, int, int> curr = dq.front();
        dq.pop_front();
        
        int x = get<0>(curr);
        int y = get<1>(curr);
        int dist = get<2>(curr);

        if (x == n - 1 && y == m - 1) {
            return dist;
        }
        
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && maps[nx][ny] == 1) {
                visited[nx][ny] = true;
                dq.push_back({nx, ny, dist + 1});
            }
        }
    }
    return -1;
}

int solution(vector<vector<int>> maps) {
    return bfs(maps);
}
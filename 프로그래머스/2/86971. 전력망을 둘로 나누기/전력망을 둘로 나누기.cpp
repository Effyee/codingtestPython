#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int find_parent(int x, vector<int>& parent) {
    if (parent[x] == x) return x;
    return parent[x] = find_parent(parent[x], parent); 
}

void make_union(int a, int b, vector<int>& parent) {
    a = find_parent(a, parent);
    b = find_parent(b, parent);
    if (a != b) {
        if (a < b) parent[b] = a;
        else parent[a] = b;
    }
}

int solution(int n, vector<vector<int>> wires) {
    int answer = n; 

    for (int i = 0; i < wires.size(); i++) {

        vector<int> parent(n + 1);
        for (int j = 1; j <= n; j++) parent[j] = j;

        for (int j = 0; j < wires.size(); j++) {
            if (i == j) continue; 
            make_union(wires[j][0], wires[j][1], parent);
        }

        int count = 0;
        int root = find_parent(1, parent);
        for (int j = 1; j <= n; j++) {
            if (find_parent(j, parent) == root) count++;
        }

        int diff = abs(count - (n - count));
        answer = min(answer, diff);
    }

    return answer;
}
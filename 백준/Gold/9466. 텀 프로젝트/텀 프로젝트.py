import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global cnt
    visited[x] = True
    next = arr[x]

    if not visited[next]:
        dfs(next)
    else:
        if not done[next]:
            temp = next
            cycle_len = 1
            while temp != x:
                temp = arr[temp]
                cycle_len += 1
            cnt += cycle_len

    done[x] = True

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))  
    visited = [False] * (n + 1)
    done = [False] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(n - cnt) 

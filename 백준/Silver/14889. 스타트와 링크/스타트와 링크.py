import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

answer = float('inf')
total = set(range(n))

# 팀 내 2명 조합 시너지 합 구하기
def team_score(team):
    res = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a, b = team[i], team[j]
            res += graph[a][b] + graph[b][a]
    return res

def comb(start=0, li=[]):
    global answer
    # 팀 A 구성 완료
    if len(li) == n//2:
        teamA = li
        teamB = list(total - set(teamA))
        diff = abs(team_score(teamA) - team_score(teamB))
        answer = min(answer, diff)
        return
    
    # 백트래킹으로 팀 A 구성
    for i in range(start, n):
        comb(i+1, li + [i])

comb()
print(answer)

def dfs(path, start, visited, tickets):
    # 모든 티켓을 사용한 경우
    if len(path) - 1 == len(tickets):
        return path

    for i in range(len(tickets)):
        if not visited[i] and start == tickets[i][0]:
            visited[i] = True  # 방문 처리
            path.append(tickets[i][1])  # 목적지 추가

            result = dfs(path, tickets[i][1], visited, tickets)
            if result:
                return result  # 유효한 경로를 찾으면 반환

            path.pop()  # 백트래킹: 마지막 추가한 목적지 제거
            visited[i] = False  # 방문 상태 되돌리기

    return None  # 유효한 경로가 없을 경우

def solution(tickets):
    visited = [False] * len(tickets)
    tickets.sort()  # 알파벳 순으로 정렬
    path = ["ICN"]  # 시작점 추가

    result = dfs(path, "ICN", visited, tickets)  # DFS 호출
    return result if result else []  # 결과 반환


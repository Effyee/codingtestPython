from collections import deque

def solution(players, m, k):
    answer = 0

    active = 0
    q = deque()

    for player in players:

        # 이번 시간 시작 전에 만료 서버 반납
        while q and q[0][0] == 0:
            _, cnt = q.popleft()
            active -= cnt

        # 남은 시간 감소
        for i in range(len(q)):
            remain, cnt = q.popleft()
            q.append((remain - 1, cnt))

        need = player // m

        if need > active:
            add = need - active

            active += add
            answer += add

            q.append((k - 1, add))

    return answer
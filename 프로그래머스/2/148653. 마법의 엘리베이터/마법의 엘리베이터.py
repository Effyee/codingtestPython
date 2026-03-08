def solution(storey):
    answer = []

    # st: 현재 층, cnt: 지금까지 사용한 돌 개수
    def dfs(st, cnt):
        # 0층이면 끝
        if st == 0:
            answer.append(cnt)
            return

        one = st % 10        # 일의 자리
        up = 10 - one        # 올려서 10으로 만드는 비용
        down = one           # 내려서 0으로 만드는 비용

        # 올리는 쪽이 더 싸면 올리기만
        if up < down:
            dfs(st // 10 + 1, cnt + up)
        elif down < up:
            dfs(st // 10, cnt + down)
        else:
            dfs(st // 10 + 1, cnt + up)   
            dfs(st // 10, cnt + down)     

    dfs(storey, 0)
    return min(answer)

def solution(n, results):
    graph = [[0] * (n) for _ in range(n)]

    for A,B in results:
        graph[A - 1][B - 1] = 1
        graph[B - 1][A - 1] = -1


    for i in range(n): #중간노드
        for j in range(n):#시작 노드
            for k in range(n):# 종점 노드
                if graph[j][k] != 0: #이미 결과가 정해져 있음
                    continue
                if graph[j][i] == 1 and graph[i][k] == 1: # j 가 i를 이기고 i가 k를 이겼으니 j 가 k를 이긴거나 마찬가지
                    graph[j][k] = 1
                elif graph[j][i] == -1 and graph[i][k] == -1: #위와 반대의 상황
                    graph[j][k] = -1

    # [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]에 대한 그래프
    # 순위를 정할때 당연히 "나"이외의 모든 노드들과 관계를 갖고 있어야 한다.
    # [0,   1,   0,  0, 1]
    # [-1,  0,  -1, -1, 1] -> 순위 확정
    # [0,   1,   0, -1, 1]
    # [0,   1,   1,  0, 1]
    # [-1, -1,  -1, -1, 0] -> 순위 확정
    answer = 0
    for g in graph:
        if len(list(filter(lambda x: x != 0,g))) == n - 1:
            answer += 1

    return answer
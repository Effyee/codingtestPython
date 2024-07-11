from collections import deque

def solution(order):
    answer = 0
    main = deque(range(1, len(order) + 1))
    sub = []

    for o in order:
        while main and main[0] <= o:
            sub.append(main.popleft())  # main 큐에서 상자를 꺼내 sub 스택에 추가

        if sub and sub[-1] == o:
            answer += 1
            sub.pop()  # sub 스택에서 상자를 꺼내 트럭에 실음
        else:
            break  # 일치하는 상자를 찾을 수 없을 경우 종료

    return answer


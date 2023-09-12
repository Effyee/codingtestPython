from collections import deque

def solution(n, m, numbers):
    answer = 0
    q = deque(numbers)

    # 리스트 값 오름차순으로 정렬
    numbers.sort()

    while True:
        if q[0] == numbers[-1]:  # 큐의 가장 앞에 있는 원소가 중요도가 가장 높은 문서일 때
            answer += 1  # 카운트 증가
            # 큐와 리스트에서 모두 해당 원소를 팝
            q.popleft()
            numbers.pop()
            if m == 0:  # m이 0일 때 == 원하는 원소가 큐의 가장 앞에 있을 때
                break
        else:
            q.append(q.popleft())
        # 원하는 원소의 위치가 0일 때 -> q의 맨 뒤로, 0이 아닐 때 -> -1.
        m = len(q) - 1 if m == 0 else m - 1

    return answer

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solution(n, m, numbers))
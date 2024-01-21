import sys

def solution(n, m, importance):
    answer = 0
    max_value = max(importance)
    i = m

    while True:
        if importance[0] == max_value:  # 현재 문서가 중요도가 가장 높은 경우
            importance.pop(0)
            answer += 1
            if i == 0:
                break
            else:
                i -= 1
            max_value = max(importance)  # 최댓값 업데이트
        else:  # 현재 문서가 중요도가 가장 높지 않은 경우
            importance.append(importance.pop(0))
            if i == 0:
                i = len(importance) - 1
            else:
                i -= 1

    return answer

a = int(sys.stdin.readline().rstrip())
answers = []
for i in range(a):
    n, m = map(int, input().split(' '))
    importance = list(map(int, sys.stdin.readline().split()))
    answers.append(solution(n, m, importance))

print('\n'.join(map(str, answers)))

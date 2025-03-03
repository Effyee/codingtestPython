import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = []

def backtrack(start):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(start, N+1):  # start 이상의 값만 선택
        answer.append(i)
        backtrack(i)  # 같은 수를 여러 번 골라도 되므로 i 그대로 넘김
        answer.pop()

backtrack(1)  # 1부터 시작

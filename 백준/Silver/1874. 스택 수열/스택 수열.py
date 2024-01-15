import sys

def solution(n, sequence):
    stack = []
    l = [i for i in range(1, n+1)]
    answer = []

    for num in sequence:
        while not stack or stack[-1] < num:
            if l and l[0] <= num:
                stack.append(l.pop(0))  # 여기서 l[0]을 pop 하면서 stack에 append 합니다.
                answer.append('+')
            else:  # l이 비어있거나 l[0]이 num보다 크면 불가능한 경우이므로 break 합니다.
                break
        if stack and stack[-1] == num:  # stack의 맨 위 원소가 num과 같다면 pop 연산을 수행합니다.
            stack.pop()
            answer.append('-')
        else:  # stack의 맨 위 원소가 num과 다르면 주어진 수열을 만들 수 없습니다.
            return 'NO'

    return '\n'.join(answer)  # 모든 연산이 성공적으로 끝났다면, 연산 과정을 문자열로 반환합니다.




n = int(sys.stdin.readline().rstrip())
sequence = []


for _ in range(n):
    sequence.append(int(sys.stdin.readline().rstrip()))

print(solution(n,sequence))
import sys
def solution(n, l):
    stack = []
    num_list = [i for i in range(1, n + 1)]
    answer = []
    for num in l:
        if num_list and num_list[0] <= num:
            while num_list and num_list[0] <= num:
                stack.append(num_list.pop(0))
                answer.append('+')
        if stack and stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            print('NO')
            return  # 'No'가 출력되면 함수를 바로 종료합니다.
    print('\n'.join(answer))


n=int(input())
l=[]
for i in range(n):
    l.append(int(sys.stdin.readline().rstrip()))

solution(n, l)

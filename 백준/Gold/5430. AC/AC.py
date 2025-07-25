import sys
from collections import deque  # pop(0)가 빈번할 때 deque 사용이 효율적

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    command = input().strip()
    n = int(input())
    arr_str = input().strip()  # 배열 문자열 '[1,2,3]' 형태

    # 1. 빈 배열 [] 입력 처리
    if arr_str == "[]":
        arr = deque()
    else:
        # 괄호 제거 후 ,로 분리하여 int로 변환 (deque 사용)
        arr = deque(map(int, arr_str[1:-1].split(',')))


    reverse_flag = 1  # 1이면 정방향, -1이면 역방향
    is_error = False

    for cmd in command:
        if cmd == 'R':
            reverse_flag *= -1  # 방향만 변경
        elif cmd == 'D':
            if not arr:  # 배열이 비어있는지 확인 (pop 하기 전에)
                print('error')
                is_error = True
                break  # command 루프 탈출

            if reverse_flag == 1:  # 정방향일 때
                arr.popleft()  # deque의 맨 앞 요소 삭제
            else:  # 역방향일 때
                arr.pop()  # deque의 맨 뒤 요소 삭제

    # 에러가 발생했다면 다음 테스트 케이스로 넘어감
    if is_error:
        continue

        # 최종 결과 출력
    if reverse_flag == -1:  # 최종 방향이 역방향이면 뒤집어서 출력
        arr.reverse()  # deque는 reverse() 메서드를 제공

    # join을 사용하여 [1,2,3] 형태의 문자열로 출력
    print('[' + ','.join(map(str, arr)) + ']')
import sys
import copy

input = sys.stdin.readline

n = int(input())
initial_board = [list(map(int, input().split())) for _ in range(n)]  # 초기 보드 저장


# --- 2048 이동 함수들 (정확한 로직으로 수정) ---

def move_right(current_board, n):
    new_board = copy.deepcopy(current_board)

    for i in range(n):  # 각 행에 대해
        # 1. 합치기 단계: 오른쪽에서 왼쪽으로 순회하며 인접한 같은 블록 합치기
        j = n - 1  # 현재 행의 가장 오른쪽(마지막) 인덱스부터 시작
        while j > 0:
            if new_board[i][j] == 0:  # 현재 칸이 0이면 무시하고 다음 칸으로
                j -= 1
                continue

            k = j - 1  # 현재 칸의 왼쪽 칸부터 탐색
            while k >= 0:
                if new_board[i][k] != 0:  # 0이 아닌 블록을 찾으면
                    if new_board[i][j] == new_board[i][k]:  # 두 블록의 값이 같으면 합칩니다.
                        new_board[i][j] *= 2
                        new_board[i][k] = 0
                        j -= 2  # 합쳐진 두 칸을 건너뛰어 다음 합치기 대상을 찾습니다.
                        break
                    else:  # 값이 다르면 합칠 수 없으므로 k 루프 종료
                        j -= 1  # 합칠 블록을 못 찾았으므로 j는 한 칸 이동
                        break
                k -= 1  # 왼쪽으로 계속 탐색
            else:  # k 루프가 break 없이 완료된 경우 (더 이상 왼쪽 블록이 없음)
                j -= 1  # j는 한 칸 이동

    # 2. 밀착 단계: 모든 합치기가 끝난 후, 0이 아닌 블록들을 오른쪽으로 몰기
    for r in range(n):
        temp_line = [val for val in new_board[r] if val != 0]  # 0이 아닌 값만 추출
        new_row = [0] * (n - len(temp_line)) + temp_line  # 앞에 0 채워서 오른쪽 정렬
        new_board[r] = new_row

    return new_board


def move_left(current_board, n):
    new_board = copy.deepcopy(current_board)

    for i in range(n):  # 각 행에 대해
        # 1. 합치기 단계: 왼쪽에서 오른쪽으로 순회하며 인접한 같은 블록 합치기
        j = 0  # 현재 행의 가장 왼쪽(첫 번째) 인덱스부터 시작
        while j < n - 1:  # j가 n-1보다 작은 동안 반복 (j+1에 접근하기 위해)
            if new_board[i][j] == 0:
                j += 1
                continue

            k = j + 1  # 현재 칸의 오른쪽 칸부터 탐색
            while k < n:
                if new_board[i][k] != 0:
                    if new_board[i][j] == new_board[i][k]:
                        new_board[i][j] *= 2
                        new_board[i][k] = 0
                        j += 2  # 합쳐진 두 칸을 건너뛰어 다음 합치기 대상을 찾습니다.
                        break
                    else:
                        j += 1  # 합칠 블록을 못 찾았으므로 j는 한 칸 이동
                        break
                k += 1  # 오른쪽으로 계속 탐색
            else:  # k 루프가 break 없이 완료된 경우 (더 이상 오른쪽 블록이 없음)
                j += 1  # j는 한 칸 이동

    # 2. 밀착 단계: 모든 합치기가 끝난 후, 0이 아닌 블록들을 왼쪽으로 몰기
    for r in range(n):
        temp_line = [val for val in new_board[r] if val != 0]
        new_row = temp_line + [0] * (n - len(temp_line))  # 뒤에 0 채워서 왼쪽 정렬
        new_board[r] = new_row

    return new_board


def move_up(current_board, n):
    new_board = copy.deepcopy(current_board)

    for c in range(n):  # 각 열에 대해
        # 1. 합치기 단계: 위에서 아래로 순회하며 인접한 같은 블록 합치기
        r = 0  # 현재 열의 가장 위쪽(첫 번째) 인덱스부터 시작
        while r < n - 1:  # r이 n-1보다 작은 동안 반복 (r+1에 접근하기 위해)
            if new_board[r][c] == 0:
                r += 1
                continue

            k = r + 1  # 현재 칸의 아래쪽 칸부터 탐색
            while k < n:
                if new_board[k][c] != 0:
                    if new_board[r][c] == new_board[k][c]:
                        new_board[r][c] *= 2
                        new_board[k][c] = 0
                        r += 2  # 합쳐진 두 칸을 건너뛰어 다음 합치기 대상을 찾습니다.
                        break
                    else:
                        r += 1  # 합칠 블록을 못 찾았으므로 r은 한 칸 이동
                        break
                k += 1  # 아래쪽으로 계속 탐색
            else:  # k 루프가 break 없이 완료된 경우
                r += 1  # r은 한 칸 이동

    # 2. 밀착 단계: 모든 합치기가 끝난 후, 0이 아닌 블록들을 위쪽으로 몰기
    for c in range(n):
        temp_column = [new_board[r][c] for r in range(n) if new_board[r][c] != 0]  # 0이 아닌 값만 추출

        # 0이 아닌 블록들로 새로운 열을 만들고, 아래 부분을 0으로 채움 (위쪽 정렬)
        for r_idx in range(n):
            if r_idx < len(temp_column):
                new_board[r_idx][c] = temp_column[r_idx]
            else:
                new_board[r_idx][c] = 0

    return new_board


def move_down(current_board, n):
    new_board = copy.deepcopy(current_board)

    for c in range(n):  # 각 열에 대해
        # 1. 합치기 단계: 아래에서 위로 순회하며 인접한 같은 블록 합치기
        r = n - 1  # 현재 열의 가장 아래쪽(마지막) 인덱스부터 시작
        while r > 0:  # r이 0보다 큰 동안 반복 (r-1에 접근하기 위해)
            if new_board[r][c] == 0:
                r -= 1
                continue

            k = r - 1  # 현재 칸의 위쪽 칸부터 탐색
            while k >= 0:
                if new_board[k][c] != 0:
                    if new_board[r][c] == new_board[k][c]:
                        new_board[r][c] *= 2
                        new_board[k][c] = 0
                        r -= 2  # 합쳐진 두 칸을 건너뛰어 다음 합치기 대상을 찾습니다.
                        break
                    else:
                        r -= 1  # 합칠 블록을 못 찾았으므로 r은 한 칸 이동
                        break
                k -= 1  # 위쪽으로 계속 탐색
            else:  # k 루프가 break 없이 완료된 경우
                r -= 1  # r은 한 칸 이동

    # 2. 밀착 단계: 모든 합치기가 끝난 후, 0이 아닌 블록들을 아래쪽으로 몰기
    for c in range(n):
        temp_column = [new_board[r][c] for r in range(n) if new_board[r][c] != 0]

        # 0이 아닌 블록들로 새로운 열을 만들고, 윗부분을 0으로 채움 (아래쪽 정렬)
        for r_idx in range(n - 1, -1, -1):  # 아래에서부터 채우기
            if (n - 1 - r_idx) < len(temp_column):  # temp_column은 아래에서부터 채워짐
                new_board[r_idx][c] = temp_column[len(temp_column) - 1 - (n - 1 - r_idx)]
            else:
                new_board[r_idx][c] = 0

    return new_board


# --- 백트래킹 로직 (수정) ---

max_block_value = 0  # 전역 변수로 최대 블록 값을 저장 (answer 대신)


def backtrack(current_board, depth):
    global max_block_value

    # 현재 보드에서 가장 큰 블록 값 업데이트
    for r in range(n):
        for c in range(n):
            max_block_value = max(max_block_value, current_board[r][c])

    # 5번 이동을 모두 마쳤으면 탐색 종료
    if depth == 5:
        return

    # 4가지 방향으로 각각 이동하며 다음 상태 탐색
    # 각 move_ 함수는 copy.deepcopy를 내부적으로 수행하므로, 여기서 추가 복사는 필요 없음.

    # 오른쪽 이동
    moved_right_board = move_right(current_board, n)
    backtrack(moved_right_board, depth + 1)

    # 왼쪽 이동
    moved_left_board = move_left(current_board, n)
    backtrack(moved_left_board, depth + 1)

    # 위쪽 이동
    moved_up_board = move_up(current_board, n)
    backtrack(moved_up_board, depth + 1)

    # 아래쪽 이동
    moved_down_board = move_down(current_board, n)
    backtrack(moved_down_board, depth + 1)


# 백트래킹 시작 (초기 보드와 0회 이동 상태로 시작)
backtrack(initial_board, 0)

print(max_block_value)
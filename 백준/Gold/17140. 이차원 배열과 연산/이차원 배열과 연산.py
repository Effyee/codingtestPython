import sys
from collections import Counter
input = sys.stdin.readline

def R_operation(A):
    new_A = []
    max_len = 0

    for row in A:
        cnt = Counter(n for n in row if n != 0)  # 0 제외
        items = sorted(cnt.items(), key=lambda x: (x[1], x[0]))  # (횟수, 숫자) 정렬

        new_row = []
        for num, freq in items:
            new_row.append(num)
            new_row.append(freq)

        max_len = max(max_len, len(new_row))
        new_A.append(new_row)

    # 모든 행 길이 맞추기, 최대 100
    for row in new_A:
        row += [0] * (max_len - len(row))
        if len(row) > 100:
            del row[100:]

    if len(new_A) > 100:
        new_A = new_A[:100]

    return new_A

def main():
    r, c, k = map(int, input().split())
    r, c = r - 1, c - 1
    A = [list(map(int, input().split())) for _ in range(3)]

    time = 0
    while True:
        if r < len(A) and c < len(A[0]) and A[r][c] == k:
            print(time)
            return

        if len(A) >= len(A[0]):  # R 연산
            A = R_operation(A)
        else:  # C 연산
            # 전치 후 R연산 후 다시 전치
            A = list(map(list, zip(*A)))
            A = R_operation(A)
            A = list(map(list, zip(*A)))

        time += 1
        if time > 100:
            print(-1)
            return

if __name__ == "__main__":
    main()

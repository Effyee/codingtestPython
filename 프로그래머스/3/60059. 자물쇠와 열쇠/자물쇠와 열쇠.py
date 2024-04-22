def rotate(key):
    m = len(key)
    rotated = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rotated[j][m - 1 - i] = key[i][j]
    return rotated


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 자물쇠를 가운데에 배치
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate(key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠를 끼워 맞춰보기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 자물쇠를 올바르게 열 수 있는지 확인
                if check(new_lock):
                    return True
                # 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False

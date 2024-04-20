def can_install(x, y, a, result):
    if a == 0:  # 기둥 설치 조건
        if y == 0 or [x-1, y, 1] in result or [x, y, 1] in result or [x, y-1, 0] in result:
            return True
    else:  # 보 설치 조건
        if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
            return True
    return False

def can_delete(x, y, a, result):
    temp = result.copy()
    temp.remove([x, y, a])
    for x, y, a in temp:
        if not can_install(x, y, a, temp):
            return False
    return True

def solution(n, build_frame):
    result = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:  # 설치
            if can_install(x, y, a, result):
                result.append([x, y, a])
        else:  # 삭제
            if can_delete(x, y, a, result):
                result.remove([x, y, a])
    result.sort()  # 결과 정렬
    return result

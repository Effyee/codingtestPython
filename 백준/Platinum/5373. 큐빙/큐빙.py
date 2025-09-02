import sys
input = sys.stdin.readline

# 각 면을 3×3으로 저장
# U(윗) D(아랫) F(앞) B(뒤) L(왼) R(오른)
def init_cube():
    return {
        'U': [['w']*3 for _ in range(3)],
        'D': [['y']*3 for _ in range(3)],
        'F': [['r']*3 for _ in range(3)],
        'B': [['o']*3 for _ in range(3)],
        'L': [['g']*3 for _ in range(3)],
        'R': [['b']*3 for _ in range(3)],
    }

# 면을 시계/반시계로 회전
def rotate_face(face, dir):
    if dir == '+':  # 시계
        return [list(row) for row in zip(*face[::-1])]
    else:  # 반시계
        return [list(row) for row in zip(*face)][::-1]

# 각 명령 처리
def rotate(cube, cmd):
    face, dir = cmd[0], cmd[1]

    # 1. 자기 자신 회전
    cube[face] = rotate_face(cube[face], dir)

    # 2. 옆 줄 교환
    if face == 'U':
        if dir == '+':
            cube['F'][0], cube['R'][0], cube['B'][0], cube['L'][0] = \
            cube['R'][0], cube['B'][0], cube['L'][0], cube['F'][0]
        else:
            cube['F'][0], cube['L'][0], cube['B'][0], cube['R'][0] = \
            cube['L'][0], cube['B'][0], cube['R'][0], cube['F'][0]

    elif face == 'D':
        if dir == '+':
            cube['F'][2], cube['L'][2], cube['B'][2], cube['R'][2] = \
            cube['L'][2], cube['B'][2], cube['R'][2], cube['F'][2]
        else:
            cube['F'][2], cube['R'][2], cube['B'][2], cube['L'][2] = \
            cube['R'][2], cube['B'][2], cube['L'][2], cube['F'][2]

    elif face == 'F':
        if dir == '+':
            tmp = [cube['U'][2][i] for i in range(3)]
            for i in range(3):
                cube['U'][2][i] = cube['L'][2-i][2]
                cube['L'][2-i][2] = cube['D'][0][2-i]
                cube['D'][0][2-i] = cube['R'][i][0]
                cube['R'][i][0] = tmp[i]
        else:
            tmp = [cube['U'][2][i] for i in range(3)]
            for i in range(3):
                cube['U'][2][i] = cube['R'][i][0]
                cube['R'][i][0] = cube['D'][0][2-i]
                cube['D'][0][2-i] = cube['L'][2-i][2]
                cube['L'][2-i][2] = tmp[i]

    elif face == 'B':
        if dir == '+':
            tmp = [cube['U'][0][i] for i in range(3)]
            for i in range(3):
                cube['U'][0][i] = cube['R'][i][2]
                cube['R'][i][2] = cube['D'][2][2-i]
                cube['D'][2][2-i] = cube['L'][2-i][0]
                cube['L'][2-i][0] = tmp[i]
        else:
            tmp = [cube['U'][0][i] for i in range(3)]
            for i in range(3):
                cube['U'][0][i] = cube['L'][2-i][0]
                cube['L'][2-i][0] = cube['D'][2][2-i]
                cube['D'][2][2-i] = cube['R'][i][2]
                cube['R'][i][2] = tmp[i]

    elif face == 'L':
        if dir == '+':
            tmp = [cube['U'][i][0] for i in range(3)]
            for i in range(3):
                cube['U'][i][0] = cube['B'][2-i][2]
                cube['B'][2-i][2] = cube['D'][i][0]
                cube['D'][i][0] = cube['F'][i][0]
                cube['F'][i][0] = tmp[i]
        else:
            tmp = [cube['U'][i][0] for i in range(3)]
            for i in range(3):
                cube['U'][i][0] = cube['F'][i][0]
                cube['F'][i][0] = cube['D'][i][0]
                cube['D'][i][0] = cube['B'][2-i][2]
                cube['B'][2-i][2] = tmp[i]

    elif face == 'R':
        if dir == '+':
            tmp = [cube['U'][i][2] for i in range(3)]
            for i in range(3):
                cube['U'][i][2] = cube['F'][i][2]
                cube['F'][i][2] = cube['D'][i][2]
                cube['D'][i][2] = cube['B'][2-i][0]
                cube['B'][2-i][0] = tmp[i]
        else:
            tmp = [cube['U'][i][2] for i in range(3)]
            for i in range(3):
                cube['U'][i][2] = cube['B'][2-i][0]
                cube['B'][2-i][0] = cube['D'][i][2]
                cube['D'][i][2] = cube['F'][i][2]
                cube['F'][i][2] = tmp[i]


# 실행
t = int(input())
for _ in range(t):
    n = int(input())
    commands = input().split()
    cube = init_cube()

    for cmd in commands:
        rotate(cube, cmd)

    # 윗면 출력
    for row in cube['U']:
        print(''.join(row))

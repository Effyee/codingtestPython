def find_space(game_board, x, y, visited, space):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited[x][y] = True
    space.append((x, y))

    n = len(game_board)
    m = len(game_board[0])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and game_board[nx][ny] == 0 and not visited[nx][ny]:
            find_space(game_board, nx, ny, visited, space)

def find_block(table, x, y, visited, block):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited[x][y] = True
    block.append((x, y))

    n = len(table)
    m = len(table[0])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 1 and not visited[nx][ny]:
            find_block(table, nx, ny, visited, block)


def normalize(shape):
    #블록이나 공간을 정규화하여 왼쪽 위를 기준으로 정렬
    min_x = min([x for x, y in shape])
    min_y = min([y for x, y in shape])
    normalized = sorted([(x - min_x, y - min_y) for x, y in shape])
    return normalized


def rotate(shape):
   #블록이나 공간을 90도 회전
    return normalize([(y, -x) for x, y in shape])


def all_rotations(shape):
    #블록이나 공간의 모든 회전 상태
    rotations = []
    current = shape
    for _ in range(4):
        current = rotate(current)
        rotations.append(current)
    return rotations


def can_place(space, block):
    #블록을 놓을 수 있는지
    return sorted(space) == sorted(block)


def solution(game_board, table):
    n = len(game_board)
    m = len(game_board[0])

    visited = [[False] * m for _ in range(n)]
    spaces = []

    for i in range(n):
        for j in range(m):
            if game_board[i][j] == 0 and not visited[i][j]:
                space = []
                find_space(game_board, i, j, visited, space)
                spaces.append(normalize(space))

    visited = [[False] * m for _ in range(n)]
    blocks = []
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1 and not visited[i][j]:
                block = []
                find_block(table, i, j, visited, block)
                blocks.append(normalize(block))

    used_blocks = [False] * len(blocks)
    total_blocks_used = 0

    for space in spaces:
        for i, block in enumerate(blocks):
            if not used_blocks[i]:
                for rotation in all_rotations(block):
                    if can_place(space, rotation):
                        used_blocks[i] = True
                        total_blocks_used += len(block)
                        break
                if used_blocks[i]:
                    break

    return total_blocks_used


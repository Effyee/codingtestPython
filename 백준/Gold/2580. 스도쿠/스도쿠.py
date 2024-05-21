def is_valid(graph, row, col, num):
    # Check if the number is not repeated in the current row
    for x in range(9):
        if graph[row][x] == num:
            return False

    # Check if the number is not repeated in the current column
    for x in range(9):
        if graph[x][col] == num:
            return False

    # Check if the number is not repeated in the current 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if graph[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(graph):
    for row in range(9):
        for col in range(9):
            if graph[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(graph, row, col, num):
                        graph[row][col] = num
                        if solve_sudoku(graph):
                            return True
                        graph[row][col] = 0
                return False
    return True

graph = []
for _ in range(9):
    graph.append(list(map(int, input().split())))

if solve_sudoku(graph):
    for row in graph:
        print(" ".join(map(str, row)))


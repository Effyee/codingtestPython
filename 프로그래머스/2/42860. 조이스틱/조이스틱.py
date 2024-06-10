def solution(name):
    def min_move(name):
        move = len(name) - 1
        for i in range(len(name)):
            next_i = i + 1
            while next_i < len(name) and name[next_i] == 'A':
                next_i += 1
            move = min(move, i + len(name) - next_i + min(i, len(name) - next_i))
        return move

    answer = 0
    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)

    answer += min_move(name)
    return answer

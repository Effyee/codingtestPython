def solution(lottos, win_nums):
    answer = []
    index = 0
    wins = 0
    for num in lottos:
        if num == 0:
            index += 1

    for win in win_nums:
        if win in lottos:
            wins += 1

    answer.append(7 - (wins + index) if wins + index > 0 else 6)
    answer.append(7 - wins if wins > 0 else 6)

    return answer

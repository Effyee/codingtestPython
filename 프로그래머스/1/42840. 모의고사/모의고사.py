def solution(answers):
    answer = []
    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answer_1[i % len(answer_1)] == answers[i]:
            cnt[0] += 1
        if answer_2[i % len(answer_2)] == answers[i]:
            cnt[1] += 1
        if answer_3[i % len(answer_3)] == answers[i]:
            cnt[2] += 1

    max_score = max(cnt)
    for i, score in enumerate(cnt):
        if score == max_score:
            answer.append(i+1)

    return answer

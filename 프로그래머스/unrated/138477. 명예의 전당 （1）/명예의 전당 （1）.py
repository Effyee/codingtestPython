from collections import deque

import heapq

def solution(k, score):
    answer = []
    l = []

    for i in range(len(score)):
        if len(l) < k:
            heapq.heappush(l, score[i])
        else:
            if l[0] < score[i]:
                heapq.heappop(l)
                heapq.heappush(l, score[i])
        answer.append(l[0])

    return answer

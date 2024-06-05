import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville and scoville[0]<K:
        if len(scoville)>=2:
            first=heapq.heappop(scoville)
            second=heapq.heappop(scoville)
            heapq.heappush(scoville,first+second*2)
        else:
            return -1
        answer+=1
    return answer
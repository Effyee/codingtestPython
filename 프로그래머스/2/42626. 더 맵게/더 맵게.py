import heapq

def solution(scoville, K):
    answer = 0
    # 스코빌 리스트 힙큐로 변경
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        
        if first >= K:
            return answer  # 첫 번째 음식이 K 이상이면 바로 반환
        
        second = heapq.heappop(scoville)  # 두 번째 음식 꺼내기
        new = first + (second * 2)  # 새로운 음식의 스코빌 지수
        heapq.heappush(scoville, new)  # 새로운 음식 추가
        
        answer += 1  # 섞은 횟수 증가
    
    # 반복 후 마지막 음식이 K 이상인지 확인
    if scoville and scoville[0] < K:
        return -1  # 모든 음식의 스코빌 지수가 K 이상이 아니면 -1 반환
    
    return answer
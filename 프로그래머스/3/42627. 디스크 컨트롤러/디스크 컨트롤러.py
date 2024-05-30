import heapq


def solution(jobs):
    # 작업을 요청 시점 기준으로 정렬
    jobs.sort()
    # 최소 힙 초기화
    heap = []
    # 현재 시간과 총 대기시간 초기화
    current_time = 0
    total_waiting_time = 0
    # 처리된 작업 수 초기화
    count = 0
    # 인덱스 초기화
    i = 0

    while count < len(jobs):
        # 현재 시간 이전에 요청된 모든 작업을 힙에 추가
        while i < len(jobs) and jobs[i][0] <= current_time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1

        if heap:
            # 힙에서 가장 짧은 작업을 꺼내서 처리
            duration, start = heapq.heappop(heap)
            current_time += duration
            total_waiting_time += current_time - start
            count += 1
        else:
            # 힙이 비어있다면 다음 작업의 요청 시점으로 이동
            current_time = jobs[i][0]

    return total_waiting_time // len(jobs)

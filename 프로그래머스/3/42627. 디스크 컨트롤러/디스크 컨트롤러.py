import heapq


def solution(jobs):
    jobs.sort()  # jobs를 시작 시간 기준으로 정렬
    answer, time, cnt, waiting_time = 0, 0, 0, 0
    now = []

    i = 0
    while cnt < len(jobs):
        # 현재 시간까지 도달한 작업들을 now 힙에 추가
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(now, (jobs[i][1], jobs[i][0]))
            i += 1

        if now:
            # 가장 소요 시간이 짧은 작업을 선택
            duration, start = heapq.heappop(now)
            time += duration
            waiting_time += time - start
            cnt += 1
        else:
            # 실행할 작업이 없으면 시간 증가
            time = jobs[i][0]

    return waiting_time // len(jobs)
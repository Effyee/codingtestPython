import heapq

def solution(jobs):
    current_time = 0
    total_times = 0  # 총 대기 시간을 저장하는 변수
    n = len(jobs)  # 작업 수
    jobs.sort()  # 작업을 시작 시간 기준으로 정렬
    job_index = 0  # 현재 처리할 작업의 인덱스
    current_jobs = []  # 현재 처리할 수 있는 작업을 저장할 힙

    while job_index < n or current_jobs:
        # 현재 시간에 처리할 수 있는 작업을 current_jobs에 추가
        while job_index < n and jobs[job_index][0] <= current_time:
            job = jobs[job_index]
            heapq.heappush(current_jobs, (job[1], job[0]))  # (소요 시간, 시작 시간)
            job_index += 1

        if current_jobs:
            # 현재 처리할 수 있는 작업이 있을 경우
            job = heapq.heappop(current_jobs)
            wait_time = current_time - job[1]  # 대기 시간 계산
            if wait_time < 0:
                wait_time = 0  # 대기 시간이 음수가 되지 않도록
            total_times += wait_time + job[0]  # 대기 시간 + 소요 시간
            current_time += job[0]  # 현재 시간 업데이트
        else:
            # 처리할 수 있는 작업이 없으면 다음 작업의 시작 시간으로 이동
            current_time = jobs[job_index][0]  # 다음 작업의 시작 시간으로 이동

    return total_times // n  # 평균 대기 시간 반환
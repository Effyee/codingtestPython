import heapq

def solution(jobs):
    time,cnt,total_time,job=0,0,0,[]
    jobs.sort()
    heapq.heapify(jobs)
    heapq.heapify(job)
    i=0
    while cnt<len(jobs):
        while i<len(jobs) and jobs[i][0]<=time:
            start,duration=jobs[i]
            heapq.heappush(job,[duration,start])
            i+=1
        if job:
            duration,start=heapq.heappop(job)
            cnt+=1
            time+=duration
            total_time+=time-start
        else:
            time=jobs[i][0]

    return total_time//len(jobs)

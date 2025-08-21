# 각 경우의 수 별로 가장 짧은 거리가 최대가 되게 하는 것
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start,end=0,distance
    while start<=end:
        mid=(start+end)//2
        prev,remove=0,0
        # 없앨 바위의 개수를 세기
        for rock in rocks:
            # 지금 간격보다 좁으면 바위를 없애기
            if rock-prev<mid:
                remove+=1
            else:
                prev=rock
        if distance-prev<mid:
            remove+=1
        
        # 바위를 n개 이상을 치워야 mid 유지 가능 -> 지금 간격이 넓음
        if remove>n:
            end=mid-1
        
        # 바위를 n개 이내로만 치워도 mid 유지 가능 -> 지금 간격이 좁음
        else:
            answer=mid
            start=mid+1
    return answer
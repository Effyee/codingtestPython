def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    # 제거할 바위의 개수
    # 최소거리, 최대 거리
    start,end=0,distance
    while start<=end:
        mid=(start+end)//2
        prev_rock,remove=0,0
        
        for rock in rocks:
            dist=rock-prev_rock
            # 지정한 거리보다 좁으면, 바위를 제거
            if dist<mid:
                remove+=1
            # 바위를 제거하지 않았다면 이전 바위의 위치를 업데이트
            else:
                prev_rock=rock
                
        if distance-prev_rock<mid:
            remove+=1
            
        # 제거한 바위가 많으면, 지정한 거리가 좁다는 뜻임
        # 거리를 넓힌다
        if remove<=n:
            answer=mid
            start=mid+1
        # 제거한 바위가 적으면, 지정한 거리가 넓다는 뜻임
        else:
            end=mid-1
    return answer
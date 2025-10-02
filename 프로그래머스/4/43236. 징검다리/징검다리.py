def solution(distance, rocks, n):
    answer = 0
    # 거리를 넓게 조건을 만족하면 저장후 거리를 넓게
    # 아니라면 거리를 좁게
    rocks.sort()
    start,end=1,distance
    while start<=end:
        mid=(start+end)//2
        prev_rock,removed=0,0
        for rock in rocks:
            # 두 개가 가까이 붙어있다면 제거
            if rock-prev_rock<mid:
                removed+=1
            else:
                prev_rock=rock
        if distance-prev_rock<mid:
            removed+=1
        # 거리를 넓히는 것, 많이 제거했다는 것, 덜 제거하겠다는 것
        if removed<=n:
            answer=mid
            start=mid+1
        else:
            end=mid-1
    return answer
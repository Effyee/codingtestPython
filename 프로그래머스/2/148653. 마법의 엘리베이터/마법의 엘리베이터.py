def solution(storey):
    answer = int(1e9)
    
    def bfs(idx, floor):
        nonlocal answer
        
        if idx >= answer:
            return
        
        if floor == 0:
            answer = min(answer, idx)
            return
        
        down = floor % 10
        up = 10 - down
        
        if down == 0:
            bfs(idx, floor // 10)
        elif down < up:
            bfs(idx + down, floor - down)
        elif down > up:
            bfs(idx + up, floor + up)
        else:
            bfs(idx + down, floor - down)
            bfs(idx + up, floor + up)

    bfs(0, storey)
    return answer
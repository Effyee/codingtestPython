def calcRainwaterInColumn(c, heights):
    # 둘러싸고 잇는 양쪽 블록 중 각각 가장 높은 블록을 구함
    left_max = max(heights[:c])
    right_max = max(heights[c + 1:])
    
    # 그 중 더 낮은 블록 높이까지 빗물이 고임
    limit = min(left_max, right_max)
    accumulated_rainwater = max(0, limit - heights[c])
    
    return accumulated_rainwater

def solution(H, W, heights):
    answer = 0
    
    # 양 끝 열에는 고일 수 없음
    for i in range(1, W - 1):
        answer += calcRainwaterInColumn(i, heights)
    
    return answer

if __name__ == "__main__":
    H, W = map(int, input().split())
    heights = list(map(int, input().split()))
    
    print(solution(H, W, heights))
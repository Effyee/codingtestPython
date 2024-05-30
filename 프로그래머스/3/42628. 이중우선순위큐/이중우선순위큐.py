import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    entry_finder = {}  # 원소의 유효성을 추적하는 dictionary
    REMOVED = '<removed-task>'  # 삭제된 원소를 표시하는 상수

    for operation in operations:
        op, num = operation.split()
        num = int(num)
        print(entry_finder)
        if op == 'I':
            # 원소를 삽입할 때, 최대 heap과 최소 heap에 각각 삽입
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
            entry_finder[num] = num
        elif op == 'D':
            if num == 1:
                # 최대 heap에서 최댓값을 삭제
                while max_heap and entry_finder.get(-max_heap[0], None) == REMOVED:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_finder[max_val] = REMOVED
            elif num == -1:
                # 최소 heap에서 최솟값을 삭제
                while min_heap and entry_finder.get(min_heap[0], None) == REMOVED:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_finder[min_val] = REMOVED

    # 유효한 최댓값과 최솟값을 찾기 위해 heap을 정리
    while max_heap and entry_finder.get(-max_heap[0], None) == REMOVED:
        heapq.heappop(max_heap)
    while min_heap and entry_finder.get(min_heap[0], None) == REMOVED:
        heapq.heappop(min_heap)

    # 결과 반환
    if max_heap and min_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]


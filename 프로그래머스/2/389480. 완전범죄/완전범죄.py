INF = int(1e9)

def solution(info, n, m):
    # arr[b] = B 흔적이 b일 때 가능한 A 흔적 최소값
    arr = [INF] * m
    arr[0] = 0

    for A, B in info:
        new_arr = [INF] * m  # 반드시 새로 만들어야 함

        for b in range(m):
            if arr[b] == INF:
                continue

            # A가 훔치는 경우
            if arr[b] + A < n:
                new_arr[b] = min(new_arr[b], arr[b] + A)

            # B가 훔치는 경우
            if b + B < m:
                new_arr[b + B] = min(new_arr[b + B], arr[b])

        arr = new_arr

    res = min(arr)
    return res if res < INF else -1

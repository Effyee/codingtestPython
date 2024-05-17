from collections import deque

# 테스트 케이스는 총 10개
for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))

    # deque를 이용하여 큐를 초기화
    password = deque(arr)

    # 사이클 반복
    n = 1
    while True:
        now = password.popleft()
        now -= n

        # 0보다 작거나 같으면 0으로 유지하고 종료
        if now <= 0:
            password.append(0)
            break
        else:
            password.append(now)

        # 감소 값 n은 1~5까지 반복
        n += 1
        if n > 5:
            n = 1

    # 결과 출력
    print(f"#{tc}", *password)

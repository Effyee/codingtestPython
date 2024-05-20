import sys
input = sys.stdin.readline

def dfs(result, index, cnt):
    global answer
    if index == n:  #nums[0]을 추가했기 때문에 실제로는 n까지가 유효 범위
        if result == s and cnt > 0:
            answer += 1
        return

    dfs(result, index + 1, cnt)  # 현재 인덱스의 숫자를 선택하지 않는 경우
    dfs(result + nums[index + 1], index + 1, cnt + 1)  # 현재 인덱스의 숫자를 선택하는 경우

n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.insert(0, 0)  # 인덱싱을 1부터 시작하기 위해 0을 추가
answer = 0
dfs(0, 0, 0)  # 첫 번째 인자를 0으로 변경
print(answer)
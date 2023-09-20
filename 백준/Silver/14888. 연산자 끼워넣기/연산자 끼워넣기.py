INF = 1000000000

def calculate(mode, op1, op2):
    if mode == 0:  # +
        return op1 + op2
    elif mode == 1:  # -
        return op1 - op2
    elif mode == 2:  # *
        return op1 * op2
    elif mode == 3:  # /
        return int(op1 / op2)  # op1 // op2 로 수행시 음수의 나눗셈에서 오류 발생

def backtracking(value, index, n, operand, operator_cnt, ans):
    if index == n:
        ans[0] = max(ans[0], value)
        ans[1] = min(ans[1], value)
        return
    for mode in range(4):
        if operator_cnt[mode] <= 0:
            continue
        operator_cnt[mode] -= 1
        next_value = calculate(mode, value, operand[index])
        backtracking(next_value, index + 1, n, operand, operator_cnt, ans)
        operator_cnt[mode] += 1

def solution(n, operand, operator_cnt):
    ans = [-INF, INF]   #ans[0]: max_value, ans[1]: min_valu

    backtracking(operand[0], 1, n, operand, operator_cnt, ans)

    return ans

if __name__ == "__main__":
    n = int(input())
    operand = list(map(int, input().split()))
    operator_cnt = list(map(int, input().split()))

    ans = solution(n, operand, operator_cnt)

    print(int(ans[0]))
    print(int(ans[1]))
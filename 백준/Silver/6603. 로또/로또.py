import sys

input = sys.stdin.readline


def solution(k, nums):
    result = []

    def backtrack(idx, li):
        if len(li) == 6:
            result.append(li[:])
            return
        if idx == k:
            return
        
        backtrack(idx + 1, li + [nums[idx]])
        backtrack(idx + 1, li)

    backtrack(0, [])
    return result


while True:
    line = input()
    if line.strip() == '0':
        break
    a = list(map(int, line.strip().split()))
    k, nums = a[0], a[1:]
    answers = solution(k, nums)
    for ans in answers:
        print(' '.join(map(str, ans)))
    print()
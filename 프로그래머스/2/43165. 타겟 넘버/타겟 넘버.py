def backtrack(numbers, result, index, target):
    if index == len(numbers):
        return 1 if result == target else 0
    return (backtrack(numbers, result + numbers[index], index + 1, target) +
            backtrack(numbers, result - numbers[index], index + 1, target))

def solution(numbers, target):
    return backtrack(numbers, 0, 0, target)

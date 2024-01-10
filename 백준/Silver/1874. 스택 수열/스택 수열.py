import sys

def solution(n, sequence):
    l = [i for i in range(1, n+1)]
    stack = []
    operations = []
    for num in sequence:
        while not stack or (l and stack[-1] < num):
            if l and l[0] <= num:
                stack.append(l.pop(0))
                operations.append('+')
            else:
                break
        if stack[-1] == num:
            stack.pop()
            operations.append('-')
        else:
            return 'NO'
    return '\n'.join(operations)

n = int(sys.stdin.readline().rstrip())
sequence = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

print(solution(n,sequence))

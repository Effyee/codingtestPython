n = int(input())
arr = list(map(int, input().split()))

def binary_search(group, x):
    start, end = 0, len(group) - 1
    while start <= end:
        mid = (start + end) // 2
        if group[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start

group = [arr[0]]

for i in range(1, n):
    if arr[i] > group[-1]:
        group.append(arr[i])
    else:
        idx = binary_search(group, arr[i])
        group[idx] = arr[i]

print(len(group))
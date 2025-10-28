N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        s = arr[i] + arr[left] + arr[right]
        if s == 0:
            if arr[left] == arr[right]:
                count = right - left + 1
                answer += count * (count - 1) // 2
                break
            else:
                l = 1
                r = 1
                while left + l < right and arr[left + l] == arr[left]:
                    l += 1
                while right - r > left and arr[right - r] == arr[right]:
                    r += 1
                answer += l * r
                left += l
                right -= r
        elif s < 0:
            left += 1
        else:
            right -= 1

print(answer)

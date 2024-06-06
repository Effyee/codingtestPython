def solution(array, commands):
    answer = []
    for command in commands:
        start,end,k=command
        arr=array[start-1:end]
        arr.sort()
        answer.append(arr[k-1])
    return answer
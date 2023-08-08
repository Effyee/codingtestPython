def solution(arr):
    answer = []
    for c in arr:
        if len(answer)==0 or answer[-1]!=c:
            answer.append(c)
    return answer
def dfs(result, cnt, alphabets, words):
    if len(result) > 5:
        return
    if result not in words:
        words.append(result)

    for i in range(len(alphabets)):
        dfs(result + alphabets[i], cnt + 1, alphabets, words)


def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    words = []
    dfs('', 0, alphabets, words)
    words.sort()

    answer = words.index(word)
    return answer

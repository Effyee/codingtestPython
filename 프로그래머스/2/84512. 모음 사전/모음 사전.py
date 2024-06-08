words=[]
def dfs(result,alphabets):
    global words
    if result not in words and len(result)<=5:
        words.append(result)
    else:
        return

    for i in range(len(alphabets)):
        if result+alphabets[i] not in words:
            dfs(result+alphabets[i],alphabets)

def solution(word):
    global words
    alphabets=['A','E','I','O','U']
    dfs('',alphabets)
    words.sort()
    answer=words.index(word)
    return answer
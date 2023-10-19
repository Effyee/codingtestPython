INF = 100000000

def solution(keymap, targets):
    answer = []
    alphas = [INF] * 30
    index = 0
    
    for key in keymap:
        for i, char in enumerate(key):
            index += 1
            if alphas[ord(char) - 65] > index:
                alphas[ord(char) - 65] = index
        index = 0
    
    for target in targets:
        total_presses = sum(alphas[ord(char) - 65] for char in target)
        
        if INF in [alphas[ord(char) - 65] for char in target]:
            answer.append(-1)
        else:
            answer.append(total_presses)
    
    return answer

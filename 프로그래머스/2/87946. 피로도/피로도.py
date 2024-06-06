from itertools import permutations
def solution(k, dungeons):
    answer = 0
    pos=[]
    for p in permutations(dungeons,len(dungeons)):
        pos.append(p)

    for i in range(len(pos)):
        cnt,stress = 0,k
        for j in range(len(dungeons)):
            if stress>=pos[i][j][0]:
                stress-=pos[i][j][1]
                cnt+=1

        answer=max(answer,cnt)
    return answer
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}


    for i, (g, p) in enumerate(zip(genres, plays)):
         #{장르1:(고유번호,재생횟수)}의 형태
        if g not in dic1:
            dic1[g] = [(i, p)]
        #{장르2:(고유번호,재생횟수)},{장르2:(고유번호,재생횟수)}의 형태
        #{'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
        else:
            dic1[g].append((i, p))
         #{장르1:재생횟수}의 형태
        #{'classic': 1450, 'pop': 3100}
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    # 재생횟수 기준 내림차순으로 정렬한다
    # 재생된 장르 k의 고유번호,재생횟수를 가져온다
    # 재생횟수에 따라서 내림차순으로 정렬한다
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    print(dic1)
    return answer
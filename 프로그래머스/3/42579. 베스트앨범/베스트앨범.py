from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dict=defaultdict(int)
    musics=[]
    for g,p in zip(genres,plays):
        genres_dict[g]+=p
    genres_dict=sorted(genres_dict.items(),key=lambda x:x[1],reverse=True)

    for i,(g,p) in enumerate(zip(genres,plays)):
        musics.append([i,g,p])
    musics=sorted(musics,key=lambda x:x[2],reverse=True)
    for g in genres_dict:
        cnt=0
        for music in musics:
            if music[1]==g[0] and cnt!=2:
                answer.append(music[0])
                cnt+=1
    return answer
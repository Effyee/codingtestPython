# 1. 많이 재생된 장르
# 2. 장르 내에서 많이 재생된 노래
# 3. 1,2가 만족되면 고유번호가 낮은 것 부터
from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_play=defaultdict(int)
    for genre,play in zip(genres,plays):
        genre_play[genre]+=play
    
    genre_play=sorted(genre_play.items(),key=lambda x:x[1],reverse=True)
    print(genre_play)
    genre_num=defaultdict(int)
    for i in range(len(genre_play)):
        genre_num[genre_play[i][0]]=i
    print(genre_num)
    li=[[] for _ in range(len(genre_play))]
    
    final=[]
    for (i,play) in enumerate(plays):
        final.append([genres[i],i,play])
    final=sorted(final,key=lambda x:x[2],reverse=True)
    print(final)
    for genre,number,play in final:
        if len(li[genre_num[genre]])<=1:
            li[genre_num[genre]].append(number)
    
    for l in li:
        answer+=l
    
    return answer
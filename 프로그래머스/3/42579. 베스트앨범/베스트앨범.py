from collections import defaultdict

def solution(genres, plays):
    genres_dict=defaultdict(int)
    plays_dict=defaultdict(list)
    for i,(genre,play) in enumerate(zip(genres,plays)):
        genres_dict[genre]+=play
        plays_dict[genre].append((play,i))

    sorted_genre = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True)
    answer=[]

    for genre,_ in sorted_genre:
        sorted_play=sorted(plays_dict[genre],key=lambda x:(-x[0],x[1]))
        answer.extend([song_id for _, song_id in sorted_play[:2]])

    return answer
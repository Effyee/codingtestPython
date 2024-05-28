from collections import defaultdict

def solution(genres, plays):
    genre_play_dict = defaultdict(int)
    song_dict = defaultdict(list)

    # 장르별 총 재생 횟수와 노래별 재생 횟수를 기록
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_dict[genre] += play
        song_dict[genre].append((play, i))

    # 장르를 총 재생 횟수가 많은 순으로 정렬
    sorted_genre_play = sorted(genre_play_dict.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for genre, _ in sorted_genre_play:
        # 각 장르별 노래를 재생 횟수가 많은 순으로 정렬하고, 재생 횟수가 같다면 고유 번호가 낮은 순으로 정렬
        sorted_songs = sorted(song_dict[genre], key=lambda x: (-x[0], x[1]))
        # 각 장르별로 최대 2개의 노래 고유 번호를 선택
        answer.extend([song_id for _, song_id in sorted_songs[:2]])
    
    return answer

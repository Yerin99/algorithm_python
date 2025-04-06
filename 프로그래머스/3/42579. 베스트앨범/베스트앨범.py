import heapq
from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = dict()
    song_dict = defaultdict(list)
    
    n = len(plays)
    for sid in range(n):
        genre, play = genres[sid], plays[sid]
        genre_dict[genre] = genre_dict.get(genre, 0) + play
        heapq.heappush(song_dict[genre], [-play, sid])  # 최대 힙
    
    genre_heap = [[-total_play, genre] for genre, total_play in genre_dict.items()]
    heapq.heapify(genre_heap)
    
    while genre_heap:
        _, hot_genre = heapq.heappop(genre_heap)
        num_songs = min(2, len(song_dict[hot_genre]))
        
        for _ in range(num_songs):
            _, sid = heapq.heappop(song_dict[hot_genre])
            answer.append(sid)
    
    return answer

import heapq

def solution(genres, plays):
    answer = []
    
    song_dict = dict() 
    genre_dict = dict()
    popular_dict = dict()
    
    genre_heap = []
    
    n = len(plays)
    
    for sid in range(n):
        genre, play = genres[sid], plays[sid]
        song_dict[sid] = [genre, play] 
        genre_dict[genre] = genre_dict.get(genre, 0) + play
        
        popular_dict[genre] = popular_dict.get(genre, [])
        heapq.heappush(popular_dict[genre], [-play, sid])
    
    for genre, total_play in genre_dict.items():
        heapq.heappush(genre_heap, [-total_play, genre])
    
    while genre_heap:
        _, hot_genre = heapq.heappop(genre_heap)
        
        for i in range(2):
            _, sid = heapq.heappop(popular_dict[hot_genre])
            answer.append(sid) 
            
            if not popular_dict[hot_genre]:
                break
            
    return answer
from collections import defaultdict


class Album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        if self.play == other.play:
            return self.track < other.track  
        return self.play > other.play

    
def solution(genres, plays):
    answer = []
    
    genre_dict = defaultdict(int)
    song_dict = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_dict[g] += p
        song_dict[g].append(Album(g, p, i))

    genre_order = sorted(genre_dict.items(), key=lambda x: x[1], reverse=True)

    for genre, _ in genre_order:
        sorted_songs = sorted(song_dict[genre],)
        answer.extend([a.track for a in sorted_songs[:2]])

    return answer
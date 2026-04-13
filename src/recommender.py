import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    songs = []
    
    with open(csv_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []
    
    # Categorical matching
    if song['genre'] == user_prefs.get('favorite_genre') or song['genre'] == user_prefs.get('genre'):
        score += 40
        reasons.append("Genre match: +40")
    
    if song['mood'] == user_prefs.get('favorite_mood') or song['mood'] == user_prefs.get('mood'):
        score += 30
        reasons.append("Mood match: +30")
    
    # Numerical proximity scoring
    def proximity_points(song_value, target_value, max_points):
        distance = abs(song_value - target_value)
        proximity = max(0, 1 - (distance / 0.5))
        return proximity * max_points
    
    # Energy proximity
    energy_score = proximity_points(song['energy'], user_prefs.get('target_energy') or user_prefs.get('energy', 0.5), 20)
    score += energy_score
    reasons.append(f"Energy proximity: +{energy_score:.1f}")
    
    # Acousticness proximity
    acousticness_score = proximity_points(song['acousticness'], user_prefs.get('target_acousticness', 0.5), 5)
    score += acousticness_score
    reasons.append(f"Acousticness proximity: +{acousticness_score:.1f}")
    
    # Danceability proximity
    danceability_score = proximity_points(song['danceability'], user_prefs.get('target_danceability', 0.5), 5)
    score += danceability_score
    reasons.append(f"Danceability proximity: +{danceability_score:.1f}")
    
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    def score_and_explain(song):
        score, reasons = score_song(user_prefs, song)
        return (song, score, ", ".join(reasons))
    
    scored_songs = [score_and_explain(song) for song in songs]
    sorted_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)
    
    # Apply diversity penalty: prevent same artist from appearing more than once
    results = []
    seen_artists = set()
    
    for song, score, explanation in sorted_songs:
        artist = song['artist']
        if artist not in seen_artists:
            results.append((song, score, explanation))
            seen_artists.add(artist)
            if len(results) == k:
                break
    
    return results
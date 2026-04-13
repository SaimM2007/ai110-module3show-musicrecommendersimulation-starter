"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs
from tabulate import tabulate


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.82,
            "target_acousticness": 0.18,
            "target_danceability": 0.79
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.40,
            "target_acousticness": 0.71,
            "target_danceability": 0.60
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.91,
            "target_acousticness": 0.10,
            "target_danceability": 0.66
        },
        "Genre Snob (Adversarial)": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.15,
            "target_acousticness": 0.95,
            "target_danceability": 0.05
        },
        "Contradictory (Adversarial)": {
            "genre": "lofi",
            "mood": "energetic",
            "energy": 0.85,
            "target_acousticness": 0.9,
            "target_danceability": 0.15
        },
        "Extreme Edges (Adversarial)": {
            "genre": "ambient",
            "mood": "contemplative",
            "energy": 0.0,
            "target_acousticness": 1.0,
            "target_danceability": 0.0
        }
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\n" + "="*70)
        print(f"🎵 {profile_name}".center(70))
        print("="*70 + "\n")

        table_data = []
        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            table_data.append([
                rank,
                song['title'],
                song['artist'],
                f"{score:.1f}/100",
                explanation
            ])

        print(tabulate(table_data, headers=["Rank", "Title", "Artist", "Score", "Reasons"], tablefmt="grid"))
        print()

if __name__ == "__main__":
    main()

"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*70)
    print("🎵 TOP MUSIC RECOMMENDATIONS 🎵".center(70))
    print("="*70 + "\n")
    
    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"#{rank}  {song['title']} by {song['artist']}")
        print(f"     Score: {score:.1f}/100")
        print(f"     Reasons:")
        for reason in explanation.split(", "):
            print(f"       • {reason}")
        print("-"*70)


if __name__ == "__main__":
    main()

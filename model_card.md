# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

GrooveMatch 1.0

---

## 2. Intended Use

This system suggests the top 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is built for classroom exploration only and is not intended for real users or production use. It assumes the user has a single, consistent taste profile and does not account for context like time of day, activity, or listening history.

**Non-intended use:** This system should not be used as a real music recommendation product. It does not have enough data, does not learn from user behavior, and does not account for cultural diversity in music taste.

---

## 3. How the Model Works

The system compares each song in the catalog against a user profile and gives it a score out of 100. Songs that match the user's preferred genre get 40 points and songs that match the preferred mood get 30 points. These are all or nothing: if the genre does not match exactly, zero points are awarded for that feature. The remaining 30 points come from how close the song's energy, acousticness, and danceability are to the user's targets. Songs are then sorted by score and the top 5 are returned.

---

## 4. Data

The catalog contains 18 songs stored in a CSV file. The original starter dataset had 10 songs covering genres like lofi, pop, rock, ambient, synthwave, jazz, and indie pop. Eight additional songs were added to cover hip-hop, classical, EDM, R&B, country, reggae, blues, and prog rock. Each song has 10 attributes: id, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The dataset is small and reflects a fairly western, English-language music taste. Genres like K-pop, Latin, and African music are not represented at all.

---

## 5. Strengths

The system works well when the user has a clear and consistent taste profile. For example the Chill Lofi profile reliably surfaced Midnight Coding and Library Rain at the top with scores above 96, which felt accurate. The High-Energy Pop profile gave Sunrise City a perfect 100 because it matched every single feature exactly. The scoring is also fully transparent: every recommendation comes with a breakdown of exactly why each song scored the way it did, which makes it easy to understand and debug.

---

## 6. Limitations and Bias

The most significant bias in this system is its over-reliance on exact genre and mood matching. Since genre and mood together account for 70 out of 100 possible points, any song that does not exactly match the user's stated genre or mood will almost never appear in the top results, even if it sounds very similar. This creates a filter bubble where a chill lofi user will repeatedly see the same 2 to 3 songs like Midnight Coding and Library Rain, with no exposure to similar-sounding songs in adjacent genres like ambient or jazz. Additionally, the energy proximity formula is harsh: any song with an energy value more than 0.5 away from the user's target scores zero points for that feature, which unfairly eliminates entire genres like classical or EDM depending on the profile. In a real product, this could mean users from less represented genres like blues, reggae, or country rarely get good recommendations since those genres have fewer songs in the dataset to match against.

---

## 7. Evaluation

I tested six user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and three adversarial profiles (Genre Snob, Contradictory, and Extreme Edges). The standard profiles worked as expected. Chill Lofi consistently surfaced Midnight Coding and Library Rain at the top, and Deep Intense Rock locked onto Storm Runner with a perfect score since it was the only rock song in the dataset. The biggest surprise was the Genre Snob adversarial profile, which asked for rock genre and intense mood but with very low energy and high acousticness. The system still ranked Storm Runner #1 with 70 points purely because of categorical matches, completely ignoring that the numerical preferences were the opposite of what a real rock song sounds like. I also ran a feature removal experiment by commenting out the mood check, which caused scores to drop by up to 30 points and reshuffled several rankings, confirming that mood is doing real work in the system.

---

## 8. Future Work

- Add soft matching for genre and mood so that similar categories like chill and relaxed get partial credit instead of zero points
- Increase the dataset size significantly so underrepresented genres like blues and reggae have more than one song to recommend
- Add a diversity constraint so the top 5 results cannot all be from the same artist or genre

---

## 9. Personal Reflection

The biggest learning moment was seeing how much the categorical weights dominated everything. I assumed numerical features like energy and acousticness would do more work, but the Genre Snob adversarial test showed that 70 points from genre and mood alone can override completely contradictory numerical preferences. Using AI tools like Copilot helped speed up the boilerplate code like loading the CSV and formatting the output, but I had to double-check the scoring logic carefully because it generated weights and formulas that did not always match the algorithm recipe I designed in Phase 2. What surprised me most was how a system this simple, basically just addition and subtraction, can still feel like it is making intelligent recommendations when the weights are tuned well. If I extended this project I would add collaborative filtering so the system could learn from what similar users actually listened to, not just what they said they preferred.
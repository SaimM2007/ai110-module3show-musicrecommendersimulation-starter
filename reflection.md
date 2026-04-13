# Reflection

## High-Energy Pop vs Chill Lofi

These two profiles produced completely opposite results. High-Energy Pop surfaced loud, fast, danceable songs like Sunrise City with a perfect 100/100, while Chill Lofi surfaced quiet, acoustic songs like Midnight Coding and Library Rain. This makes sense because energy and acousticness pull in opposite directions for these two profiles.

## Chill Lofi vs Deep Intense Rock

Both profiles found their top match easily since each had a clear genre match in the dataset. But Deep Intense Rock only had one real match (Storm Runner) while Chill Lofi had three strong matches. This shows that underrepresented genres get worse recommendations.

## Genre Snob vs Contradictory (Adversarial)

The Genre Snob profile proved that categorical weights dominate everything. Storm Runner ranked #1 even though its energy and acousticness were the complete opposite of what the profile asked for. The Contradictory profile showed the opposite problem: when genre and mood conflict with numerical preferences, no song scores well and the top results all feel like compromises.

## Extreme Edges (Adversarial)

Asking for energy 0.0 and danceability 0.0 broke the proximity formula because no songs in the dataset are that extreme. Almost every song scored near zero for those features, making the recommendations feel random. This shows the system needs guard rails for unrealistic input values.
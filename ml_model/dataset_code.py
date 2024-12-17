import numpy as np
import pandas as pd

# Generate a dataset with random values
np.random.seed(42)

# Features: video_length (seconds), complexity_score (1-10 scale)
video_length = np.random.uniform(30, 600, 100)  # 100 videos with lengths between 30s and 10min
complexity_score = np.random.uniform(1, 10, 100)

# Labels: time_to_complete (translation time in seconds)
time_to_complete = video_length * complexity_score * np.random.uniform(0.5, 1.5, 100)

# Create a DataFrame
df = pd.DataFrame({
    'video_length': video_length,
    'complexity_score': complexity_score,
    'time_to_complete': time_to_complete
})

# Save dataset to a CSV file
df.to_csv('video_translation_data.csv', index=False)

print(df.head())

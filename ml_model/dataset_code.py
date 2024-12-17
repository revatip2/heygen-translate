import numpy as np
import pandas as pd

np.random.seed(42)

video_length = np.random.uniform(30, 600, 100)  
complexity_score = np.random.uniform(1, 10, 100)

time_to_complete = video_length * complexity_score * np.random.uniform(0.5, 1.5, 100)

df = pd.DataFrame({
    'video_length': video_length,
    'complexity_score': complexity_score,
    'time_to_complete': time_to_complete
})

# Save dataset to a CSV file
df.to_csv('video_translation_data.csv', index=False)

print(df.head())

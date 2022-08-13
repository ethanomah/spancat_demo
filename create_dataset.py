import pandas as pd
import json
from pathlib import Path

f_path = Path('./data/job_dataset.csv')

df = pd.read_csv(f_path, sep=',')

sample_df = df.sample(n=500, random_state=42)

texts = [{"text" : text} for text in sample_df["job_summary"]]

out_path = Path('./data/job_summaries_sample.json')

with open(out_path, 'w') as outfile:
    json.dump(texts, outfile, indent=4)


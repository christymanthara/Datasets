import pandas as pd

df = pd.read_csv("../extracted_csv/GSM2230757_human1_umifm_counts.csv.gz", compression="gzip")
print(df.head())  # Display first few rows

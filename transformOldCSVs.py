import pandas as pd
import os

# Define input and output paths
input_file = '/home/pete/repos/gbb-historical-data/historical-csvs/Season_1.csv'
output_folder = '/home/pete/repos/gbb-historical-data/transformed-csvs'
output_file = os.path.join(output_folder, 'gbb_transformed_data.csv')

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Read the CSV
df = pd.read_csv(input_file)

# (Optional) Perform any cleaning or transformation here
# For example: df.columns = [col.strip().lower() for col in df.columns]

# Write to new CSV
df.to_csv(output_file, index=False)

print(f"CSV written to {output_file}")

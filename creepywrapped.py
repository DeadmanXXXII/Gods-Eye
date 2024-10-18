import os

# Define the target username and output path
username = "target_username"
output_file = f"/path/to/output/{username}_creepy_output.csv"

# Run Creepy from command line (adjust path to creepy as needed)
os.system(f"creepy --user {username} --output {output_file}")

# Parse and analyze the output CSV
import pandas as pd
data = pd.read_csv(output_file)

# Process the geolocation data (for example, plotting it on a map)
for index, row in data.iterrows():
    print(f"Location: {row['latitude']}, {row['longitude']}, Date: {row['timestamp']}")

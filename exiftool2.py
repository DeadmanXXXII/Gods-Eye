import subprocess
import json

# Function to extract metadata using ExifTool
def extract_metadata(file_path):
    result = subprocess.run(['exiftool', '-json', file_path], stdout=subprocess.PIPE)
    metadata = json.loads(result.stdout.decode('utf-8'))
    return metadata

# Test the function
metadata = extract_metadata('image.jpg')
print(metadata)

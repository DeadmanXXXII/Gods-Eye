import subprocess
import os

def extract_metadata(file_path):
    result = subprocess.run(['exiftool', '-json', file_path], stdout=subprocess.PIPE)
    metadata = result.stdout.decode('utf-8')
    return metadata

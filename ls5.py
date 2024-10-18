from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import os

# Path to your chromedriver and ExifTool
chrome_driver_path = '/usr/bin/chromedriver'
exiftool_path = '/usr/bin/exiftool'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Ensure GUI is not needed
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the Chrome driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    url = "https://www.facebook.com/people/Mude-seu-Mundo/100064758844407/"
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Example: Scrape all links
    links = driver.find_elements(By.TAG_NAME, 'a')
    for link in links:
        print(link.get_attribute('href'))

    # Download an image for metadata extraction
    image_url = "https://example.com/image.jpg"  # Replace with the actual image URL
    image_path = "/path/to/downloaded/image.jpg"
    os.system(f"wget {image_url} -O {image_path}")

    # Extract metadata using ExifTool
    metadata = subprocess.run([exiftool_path, '-json', image_path], stdout=subprocess.PIPE)
    print(metadata.stdout.decode())

finally:
    # Clean up
    driver.quit()

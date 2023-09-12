import time
from selenium import webdriver
from bs4 import BeautifulSoup

# URL of the Amazon product page
url = "https://www.amazon.com/dp/YourProductIDHere"

# Initialize the Selenium webdriver (you can change the path to your WebDriver)
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Navigate to the Amazon product page
driver.get(url)

# Wait for the page to load (you may need to adjust the wait time)
time.sleep(5)

# Get the page source using Selenium
page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Extract the details you want
product_title = soup.find("span", {"id": "productTitle"}).text.strip()
product_image_url = soup.find("img", {"id": "landingImage"})["src"]
product_price = soup.find("span", {"id": "priceblock_ourprice"}).text.strip()
product_details = soup.find("div", {"id": "productDescription"}).text.strip()

# Print the scraped details
print("Product Title:", product_title)
print("Product Image URL:", product_image_url)
print("Price of the Product:", product_price)
print("Product Details:", product_details)

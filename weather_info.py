from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ask user for place
place = input("Enter the place you want the weather for: ")

# Set up the webdriver (make sure chromedriver is installed and in PATH)
driver = webdriver.Chrome()

try:
    driver.get("https://www.metoffice.gov.uk/")

    # Wait for the search input box to be clickable
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "txtSearch"))
    )

    # Type the user input place
    search_input.send_keys(place)
    search_input.send_keys(Keys.RETURN)

    # Wait for the weather forecast page to load
    forecast_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "forecast"))
    )

    # Grab the weather summary text
    summary = driver.find_element(By.CLASS_NAME, "summary").text
    print(f"Weather summary for {place}:")
    print(summary)

finally:
    driver.quit()

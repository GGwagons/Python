from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def startBot(username, password, url):
    # Paths to geckodriver and Firefox binary
    geckodriver_path = "/snap/bin/geckodriver"  # Update this
    firefox_binary_path = "usr/lib/firefox"  # Update this if necessary

    # Configure Firefox options and service
    options = Options()
    options.binary_location = firefox_binary_path
    service = Service(executable_path=geckodriver_path)

    # Initialize the WebDriver
    driver = webdriver.Firefox(service=service, options=options)

    # Navigate to the target URL and perform actions
    driver.get(url)

      # Wait for the username field to be visible
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

    # Fill in the login details
    inputElement = driver.find_element("name", "username")
    inputElement.send_keys(username)

    inputElement = driver.find_element("name", "password")
    inputElement.send_keys(password)

    # Submit the form
    inputElement.submit()
    
     # Wait for the page to load after submission
    WebDriverWait(driver, 500).until(EC.title_contains("Logged In"))  # Update with the title or condition you expect


    # Print the title of the current page
    print(driver.title)

    # Close the browser window
    driver.quit()

# Read the info from info.txt
info_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'info.txt')
with open(info_path, 'r') as file:
    lines = file.readlines()
    username = lines[0].strip()
    print(username)
    password = lines[1].strip()
    print(password)
    urls = lines[2].strip().split(',')

for url in urls:
    startBot(username, password, url)


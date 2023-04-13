from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# Define the elements to interact with as an array
elements = ["answers[253889]", "answers[253889]"]

# Set the number of runs for the script to perform
num_runs = 3

# Set up the browser options to simulate incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--disable-geolocation")


# Loop through the number of runs
for i in range(num_runs):
    driver = webdriver.Chrome(options=chrome_options, executable_path=ChromeDriverManager().install())
    actions = ActionChains(driver)

    # Navigate to the website
    driver.get("https://www.bizjournals.com/chicago/pulse/survey/chicago-inno-madness-2023-semifinals/22234257")

    radio = driver.find_element(By.NAME, elements[random.randint(0, 1)])
    actions.move_to_element(radio).perform()
    radio.click()

    # Wait for a convincing amount of time
    time.sleep(1)

    # Click the "Next Question" button
    next_button = driver.find_element(By.CSS_SELECTOR, "#pulse-next-question-1")
    next_button.click()

    # Wait for the second radio button to be clickable
    radio2 = driver.find_element(By.NAME, "answers[253890]")
    actions2 = ActionChains(driver)
    actions2.move_to_element(radio2).perform()
    radio2.click()

    # Wait for a convincing amount of time
    time.sleep(1)

    # Click the "Submit" button
    submit_button = driver.find_element(By.CSS_SELECTOR, "#formSubmit")
    actions3 = ActionChains(driver)
    actions3.move_to_element(submit_button).perform()
    submit_button.click()

    driver.close()
    driver.quit()
    # Close the browser

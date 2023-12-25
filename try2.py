from selenium import webdriver
import time
import pickle
import os

options = webdriver.FirefoxOptions()
#options.add_argument("--start-maximized")

current_directory = os.path.dirname(os.path.realpath(__file__))
driver_path = os.path.join(current_directory, 'geckodriver')

driver = webdriver.Firefox(executable_path=driver_path)
#driver.maximize_window()


# Load the cookies from the file
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)

# Visit the desired website
driver.get("https://www.basketball24.com/usa/nba/results/")

# Add the loaded cookies to the browser session
for cookie in cookies:
    driver.add_cookie(cookie)
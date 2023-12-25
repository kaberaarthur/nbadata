from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

options = webdriver.FirefoxOptions()
#options.add_argument("--start-maximized")
options.headless = True

current_directory = os.path.dirname(os.path.realpath(__file__))
driver_path = os.path.join(current_directory, 'geckodriver')

driver = webdriver.Firefox(executable_path=driver_path, options = options)
#driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://google.com")

time.sleep(10)

driver.quit()
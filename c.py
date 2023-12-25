from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import re
import os
import time
import firebase_admin
from firebase_admin import credentials, firestore

# Use the service account credentials JSON file you downloaded from Firebase
cred = credentials.Certificate('nba-history.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

options = webdriver.FirefoxOptions()
#options.add_argument("--start-maximized")

current_directory = os.path.dirname(os.path.realpath(__file__))
driver_path = os.path.join(current_directory, 'geckodriver')

driver = webdriver.Firefox(executable_path=driver_path)
#driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.basketball24.com/usa/nba/results/")

datetime_one = datetime.now()
print("Current Date and Time:", datetime_one)

cb = 0
count = 0

while count < 20:    
    time.sleep(10)

    #Accept Cookies
    cookies = driver.find_elements_by_xpath("//*[contains(text(), 'I Accept')]")
    if len(cookies) > 0:
        if cb > 0:
            print("Cookies Already Accepted")
        else:
            cookies[0].click()
            cb += 1
    
    time.sleep(5)
    elements = driver.find_elements_by_xpath("//*[contains(text(), 'Show more matches')]")
    # If found, click the element
    if len(elements) > 0:
        elements[0].click()
    else:
        break

    count += 1
    print("Current Count: " + str(count))
        

datetime_two = datetime.now()
print("Current Date and Time:", datetime_two)

# Find all elements with the class name '.event__match'
matches = driver.find_elements_by_class_name("event__match")

# Extract and print the ID of each element
for match in matches:
    match_id = match.get_attribute("id")
    event_time_element = match.find_element_by_class_name("event__time")
    event_time = event_time_element.text
    extracted_id = re.sub(r'^g_3_', '', match_id)

    # Check if 'AOT' exists in the string
    if 'AOT' in event_time:
        # Remove 'AOT' if it exists in the string
        event_time = event_time.replace('AOT', '')

    # Remove any new lines and spaces from the string
    event_time = event_time.replace('\n', '').replace(' ', '')

    date_format = "%d.%m.%H:%M"  # Month-Day Hour:Minute
    parsed_time = datetime.strptime(event_time, date_format)
    
    if parsed_time.year == 1900:
        # If the year is default (1900), set it to 2023
        parsed_time = parsed_time.replace(year=2023)

    event_time = parsed_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    #print("Element ID:", extracted_id)
    #print("Event Time:", event_time)

    data = {
        'gameID': extracted_id,
        'time': event_time  # Format this as per your requirement
    }

    # Add data to the 'games-23-24' collection, creating a new document
    doc_ref = db.collection('games-23-24').document()
    doc_ref.set(data)

    print("Document created with ID:", doc_ref.id)

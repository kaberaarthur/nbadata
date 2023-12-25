from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
import re
import os
import time

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

time.sleep(10)

gameID = "IVwhv8bn"

driver.get("https://www.basketball24.com/match/" + gameID + "/#/odds-comparison/home-away/ft-including-ot")

home_team = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div[2]/a").text
away_team = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[4]/div[3]/div[1]/a").text

home_score = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[3]/div/div[1]/span[1]").text
away_score = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[3]/div/div[1]/span[3]").text


print(home_team + " Vs. " + away_team)
print("Home: " + str(home_score) + " - Away: " + str(away_score))

if int(home_score) > int(away_score):
    print("Home Team Won")
else:
    print("Away Team Won")


#### HOME ODDS ####
# Check old and new Odds (AA)
bm_one_home = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[1]/a[1]").get_attribute('title')
if len(bm_one_home) > 0:
    bm_one_home_start = bm_one_home.split(" » ")[0]
else:
    bm_one_home_start = ""

bm_one_home_last = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[1]/a[1]/span").text


if len(bm_one_home_start) == 0:
    bm_one_home_start = bm_one_home_last

print(bm_one_home_start)
print(bm_one_home_last)


# Check old and new Odds (BA)
bm_two_home = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[2]/a[1]").get_attribute('title')
if len(bm_two_home) > 0:
    bm_two_home_start = bm_two_home.split(" » ")[0]
else:
    bm_two_home_start = ""

bm_two_home_last = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[2]/a[1]/span").text


if len(bm_two_home_start) == 0:
    bm_two_home_start = bm_two_home_last

print(bm_two_home_start)
print(bm_two_home_last)


# Check old and new Odds (CA)
bm_three_home = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[3]/a[1]").get_attribute('title')
if len(bm_three_home) > 0:
    bm_three_home_start = bm_three_home.split(" » ")[0]
else:
    bm_three_home_start = ""

bm_three_home_last = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[3]/a[1]/span").text


if len(bm_three_home_start) == 0:
    bm_three_home_start = bm_three_home_last

print(bm_three_home_start)
print(bm_three_home_last)


# Check old and new Odds (DA)
bm_four_home = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[4]/a[1]").get_attribute('title')
if len(bm_four_home) > 0:
    bm_four_home_start = bm_three_home.split(" » ")[0]
else:
    bm_four_home_start = ""

bm_four_home_last = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[4]/a[1]/span").text


if len(bm_four_home_start) == 0:
    bm_four_home_start = bm_four_home_last

print(bm_four_home_start)
print(bm_four_home_last)


#### AWAY ODDS ####
# Check old and new Odds (AA)
bm_one_away = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[1]/a[2]").get_attribute('title')
if len(bm_one_away) > 0:
    bm_one_away_start = bm_one_away.split(" » ")[0]
else:
    bm_one_away_start = ""

bm_one_away_last = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[1]/a[2]/span").text


if len(bm_one_away_start) == 0:
    bm_one_away_start = bm_one_away_last

print(bm_one_away_start)
print(bm_one_away_last)


# Check old and new Odds (BA)
bm_two_away = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[2]/a[2]").get_attribute('title')
if len(bm_two_away) > 0:
    bm_two_away_start = bm_two_away.split(" » ")[0]
else:
    bm_two_away_start = ""

bm_two_away_last = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[2]/a[2]/span").text


if len(bm_two_away_start) == 0:
    bm_two_away_start = bm_two_away_last

print(bm_two_away_start)
print(bm_two_away_last)


# Check old and new Odds (CA)
bm_three_away = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[3]/a[2]").get_attribute('title')
if len(bm_three_away) > 0:
    bm_three_away_start = bm_three_away.split(" » ")[0]
else:
    bm_three_away_start = ""

bm_three_away_last = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[3]/a[2]/span").text


if len(bm_three_away_start) == 0:
    bm_three_away_start = bm_three_away_last

print(bm_three_away_start)
print(bm_three_away_last)


# Check old and new Odds (DA)
bm_four_away = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[4]/a[2]").get_attribute('title')
if len(bm_four_away) > 0:
    bm_four_away_start = bm_three_away.split(" » ")[0]
else:
    bm_four_away_start = ""

bm_four_away_last = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[3]/div/div[2]/div[4]/a[2]/span").text


if len(bm_four_away_start) == 0:
    bm_four_away_start = bm_four_away_last

print(bm_four_away_start)
print(bm_four_away_last)


#### Insert Into Firestore ####
data = {
    'gameID': gameID,
    'homeTeam': home_team,
    'awayTeam': away_team,
    'homeScore': home_score,
    'awayScore': away_score,

    'bmOneHomeStart': bm_one_home_start,
    'bmOneHomeLast': bm_one_home_last,
    'bmTwoHomeStart': bm_two_home_start,
    'bmTwoHomeLast': bm_two_home_last,
    'bmThreeHomeStart': bm_three_home_start,
    'bmThreeHomeLast': bm_three_home_last,
    'bmFourHomeStart': bm_four_home_start,
    'bmFourHomeLast': bm_four_home_last,

    'bmOneAwayStart': bm_one_away_start,
    'bmOneAwayLast': bm_one_away_last,
    'bmTwoAwayStart': bm_two_away_start,
    'bmTwoAwayLast': bm_two_away_last,
    'bmThreeAwayStart': bm_three_away_start,
    'bmThreeAwayLast': bm_three_away_last,
    'bmFourAwayStart': bm_four_away_start,
    'bmFourAwayLast': bm_four_away_last,
}

# Add data to the 'games-23-24' collection, creating a new document
doc_ref = db.collection('history-23-24').document()
doc_ref.set(data)

print("Document created with ID:", doc_ref.id)
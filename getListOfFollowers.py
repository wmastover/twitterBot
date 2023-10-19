from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
from saveAsCSV import saveAsCSV
from twitterLogon import twitterLogon
from readCSV import readCSV

#go through an autotrader search and get the   

def removeDupes(input_list):
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)

    return unique_list


def getListToMessage(driver, twitterHandle):
    

    time.sleep(3)

    # go to the followers page of the account you are trying to scrape
    driver.get("https://twitter.com/" + twitterHandle + "/followers")

    time.sleep(5)

    filename = (twitterHandle + "Followers.csv")

    currentList = []
    try:
        array = readCSV(filename)

        for item in array:
            currentList.append(item[1])

    except:
        print("no current followers file: " + filename)
    

    counter = 0
    while counter < 200:

        counter = counter + 1

        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for new content to load
        time.sleep(7)
        
        # Check if the scrollHeight has changed
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == driver.execute_script("return window.pageYOffset + window.innerHeight"):
            print()
        
        # get the list of followers who are curretnly visibit
        listOfFollowers = driver.find_elements(By.CSS_SELECTOR, '[data-testid="UserCell"]')

        followers = []
        for x in listOfFollowers:
            follower = x.find_element(By.TAG_NAME, "a").get_attribute("href")
            followers.append(follower)
        
        
        # Add visible followers on the page to previous list then remove duplicates
        currentList = [*currentList, *followers]
        currentList = removeDupes(currentList)
            
        saveList = []

        for x in currentList:
            saveList.append([0,x])
        
        
        saveAsCSV(saveList, filename)

    



        



    # Get scroll height


# js5668301@gmail.com
# @JohnSmi23124180
# Alpaca699

    


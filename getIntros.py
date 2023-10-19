from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import csv
from saveAsCSV import saveAsCSV
from readCSV import readCSV
from getOneLine import getOneLine


#go through an autotrader search and get the   




def getArticleBody(driver, element):

    def getAllText(element):
        if element.text:
            yield element.text
        for child in element.find_elements(By.XPATH, "./*"):
            yield from getAllText(child)

    text_content = list(getAllText(element))
    final_list = []
    for fragment in text_content:
            if fragment not in final_list:
                final_list.append(fragment)
            
    print(final_list)
    formatted_text = f"""\n""".join(final_list)
    return final_list[0].replace("\n", "")



def getIntros(driver, followers):
    
    company = followers.replace("Followers.csv","")
    filename = company + "OutreachList.csv"


    time.sleep(3)

    accounts = readCSV(followers)
    usersOutreach = []
    try:
        array = readCSV(filename)

        for item in array:
            usersOutreach.append(item)

    except:
        print("no current followers file: " + filename)

    for account in accounts:
        saveAsCSV(usersOutreach, filename)\
        

        driver.get(account[1])

        time.sleep(5)

        userName = account[1].replace("https://twitter.com/","")
        try:
            
            # If this fails, try block will exit, hacky but it workds
            DMElement = driver.find_element(By.XPATH, '//div[@data-testid="sendDMFromProfile"]')          
            
            timeline = driver.find_element(By.XPATH, '//div[starts-with(@aria-label, "Timeline:")]')

            # get list of elements containing the tweet information
            tweetsList = timeline.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]')

            # get user description / bio
            userDescriptionContainer = driver.find_element(By.XPATH, './/div[@data-testid="UserDescription"]')

            userDescription = getArticleBody(driver, userDescriptionContainer)

            # create tweets section of query
            queryText =  f"""

                    User Name: {userName}

                    User Description: {userDescription}

            """

            for x in tweetsList:
                
                # get the username from the tweet (incase its an RT)
                try:
                    tweetUser = x.find_element(By.XPATH, './/div[@data-testid="User-Name"]//a').get_attribute("href")

                    # get the text of the tweet
                    tweetText = x.find_element(By.XPATH, './/div[@data-testid="tweetText"]//span').text

                except:
                    tweetText = ""
                    tweetUser = ""

                
                # check if the user
                if tweetUser == account[1]:
                    
                    queryText =  queryText + f"""

                    User Tweet: {tweetText}

                    """

                print(queryText)

                
            oneLine = getOneLine(queryText)

            usersOutreach.append([account[1], userDescription, oneLine])

                
        except Exception as e:
            # Code to handle the exception
            print(f"An error occurred: {e}")

    
            

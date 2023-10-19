from getListOfFollowers import getListToMessage
from getIntros import getIntros
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from twitterLogon import twitterLogon


chromedriver = ChromeDriverManager().install()
driver = webdriver.Chrome(chromedriver )
driver.get("https://twitter.com/login")

twitterLogon("js5668301@gmail.com", "SecondBrainAnna",  "Frontdoor2023", driver)

getIntros(driver, "obsdmdFollowers.csv")

# for account in array:
#     getListToMessage(driver, account)

#     # filename = account + "Followers.csv"

#     # getIntros(driver, filename)


# js5668301@gmail.com
# @FrontdoorAnna
# Frontdoor2023

# wmabetting@gmail.com
# @FrontdoorWill
# Frontdoor2023
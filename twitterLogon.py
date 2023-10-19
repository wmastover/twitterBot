from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromedriver = ChromeDriverManager().install()

webdriver_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=webdriver_service)


def twitterLogon(email, username, password, driver):

    driver.get("https://twitter.com/login")
    time.sleep(10)

    emailLabel = driver.find_element(By.XPATH, "//span[contains(text(), 'Phone, email address, or username')]/ancestor::label[1]")

    emailInput = emailLabel.find_element( By.XPATH, ".//input[1]")

    emailInput.send_keys(email)

    time.sleep(1)

    nextButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")

    nextButton = nextButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

    nextButton.click()

    time.sleep(5)

    try:
        title = driver.find_element(By.XPATH, "//span[contains(text(), 'Enter your phone number or username')]")
        
        print("enter phone number or username found")

        usernameInput = driver.find_element(By.TAG_NAME, "input")

        usernameInput.send_keys(username)

        time.sleep(1)

        nextButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")

        nextButton = nextButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

        nextButton.click()



    except:
        print("phone number / username not requested")

    time.sleep(5)

    passwordLabel = driver.find_element(By.XPATH, "//span[contains(text(), 'Password')]/ancestor::label[1]")

    passwordInput = passwordLabel.find_element( By.XPATH, ".//input[1]")

    passwordInput.send_keys(password)

    time.sleep(1)

    LoginButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")

    LoginButton = LoginButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

    LoginButton.click()

    time.sleep(5)



# twitterLogon("js5668301@gmail.com", "SecondBrainAnna",  "Frontdoor2023", driver)

# twitterLogon("wmabetting@gmail.com", "FrontdoorWill",  "Frontdoor2023", driver)
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def score_check(site_a):
    chromeOptions = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path="/home/ben/PycharmProjects/class8/web-and-automation/solution/chromedriver123")
    chrome_driver.get(site_a)
    web_score = int(chrome_driver.find_element(by=By.XPATH, value="/html/body/h1/div").text)
    chrome_driver.close()
    if 1<=web_score<=1000:
        return True
    else:
        return False

def main_function():
    if score_check('http://172.17.0.2:5001/')==True:
        sys.exit(0)
    else:
        sys.exit(-1)


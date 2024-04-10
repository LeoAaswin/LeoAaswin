from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
service = Service('C:\\Users\\nisha\\Desktop\\chromedriver\\chromedriver.exe')


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-self-shm-usage")
    options.add_argument("--no-sendbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    """From Which websites we want to scrape the data"""
    driver.get("https://automated.pythonanywhere.com/login/") 
    return driver


def main():
    driver = get_driver()

    driver.find_element(by="id",value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id",value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    print(driver.current_url)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)



print(main())

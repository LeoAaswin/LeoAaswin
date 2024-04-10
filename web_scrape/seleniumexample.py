"""Dynamic Web Scraping"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver


def clean_text(text):
    """Extract only the temperature from the text"""
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    temperature = clean_text(element.text)
    driver.quit()
    return temperature


print(main())

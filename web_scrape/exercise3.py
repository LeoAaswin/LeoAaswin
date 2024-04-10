from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service('C:\\Users\\nisha\\Desktop\\chromedriver\\chromedriver.exe')


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable--dev-self-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service,options=options)
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver

def main():
    driver = get_driver()

    driver.find_element(by="id",value="CustomerEmail").send_keys("dhakalaaswin45@gmail.com")
    time.sleep(2)
    driver.find_element(by="id",value="CustomerPassword").send_keys("Aaswin")
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/main/article/section/div/div[1]/form/button").click()
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    time.sleep(3)
    print(driver.current_url)


print(main())



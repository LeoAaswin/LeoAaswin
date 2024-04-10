from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime as dt

def get_driver():
    service = Service('C:\\Users\\nisha\\Desktop\\chromedriver\\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-self-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def clean_text(text):
    """Extract only the temperature from the text"""
    output = float(text.split(": ")[1])
    return output

def write_file(text):
    """write the input text into a text file"""
    filename = f"{('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        temperature = str(clean_text(element.text))
        write_file(temperature)
        driver.quit()  # Don't forget to quit the driver after use
        return temperature

print(main())
